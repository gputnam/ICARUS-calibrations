import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import datetime as dt
from lib.ntuple_glob import NTupleGlob
from lib import branches
import numpy as np
import pandas as pd

# load constants
from lib.constants import *

import os

# Script parameters
NCHUNK = 10
PLANE = 2
SPNAME = "sp"
SAVEMC = False

plane2branches = [
    "h.%s.x" % SPNAME, "h.%s.y" % SPNAME, "h.%s.z" % SPNAME, "h.time", "h.tpc", "h.wire", "h.integral", "pitch", "h.sumadc", "i_snippet", "h.width"
]
if SAVEMC:
    plane2branches.append("h.channel")

plane2branches = ["hits%i.%s" % (PLANE, s) for s in plane2branches]

truehitbranches = [
    "channel", "ndep", "nelec", "e", "pitch",
]
truehitbranches = ["truth.p.truehits%i.%s" % (PLANE, s) for s in truehitbranches]

def isTPCE(df):
    return df.tpc <= 1

def reduce_df(df, truedf=None):
    if len(df) == 0: # Ignore empty df's 
        return None

    select_track = (df.selected == 1) & (df.length > 25) & ~np.isnan(df.t0PFP)

    hits = df["hits%i" % PLANE]
    
    df = df[(hits.pitch > 0) & select_track].copy()
    df["chunk"] = df.index.get_level_values(1) // NCHUNK
    df["tpcE"] = isTPCE(hits.h)
    # Ignore hits that are not the first in a snippet on a track.
    # In the aggregation function (median) below, these entries will
    # be skipped in the computation
    df.loc[hits.i_snippet > 0, ("h", "sumadc", "", "")] = np.nan 

    # Add in truth if we can
    if truedf is not None:
        truedf = truedf.truth.p["truehits%i" % PLANE]
        truedf.columns = pd.MultiIndex.from_tuples([("true_" + s, '', '', '') for s in truedf.columns]) 
        df = df.merge(truedf, left_on=['entry', ('hits%i' % PLANE, 'h', 'channel', '')], 
                                          right_on=['entry', ('true_channel', '', '', '')],
                                          how="left", validate="many_to_one")
    else:
        df["true_nelec"] = -1.
        df["true_e"] = -1.
        df["true_pitch"] = -1.

    hitsname = "hits%i" % PLANE

    outdf = df.groupby(["entry", "chunk"])[[(hitsname, 'h', 'integral', ''),
                                            (hitsname, 'h', 'sumadc', '', ),
                                            (hitsname, 'pitch', '', ''),
                                            ('true_nelec', '', '', ''),
                                            ('true_e', '', '', ''),
                                            ('true_pitch', '', '', ''),
                                          ]].sum()

    outdf = outdf.join(df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'x'),
                                                      (hitsname, 'h', SPNAME, 'y'),
                                                      (hitsname, 'h', SPNAME, 'z'),
                                                      (hitsname, 'h', 'time', ''),
                                                      (hitsname, 'h', 'width', ''),
                                                     ]].mean())
    outdf.columns = ["charge", "sumadc", 'pitch', 'true_nelec', 'true_e', "true_pitch", "x", "y", "z", "time", "width"]

    dx = df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'x')]].first() - df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'x')]].last()
    dy = df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'y')]].first() - df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'y')]].last()
    dz = df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'z')]].first() - df.groupby(["entry", "chunk"])[[(hitsname, 'h', SPNAME, 'z')]].last()
    dx = dx.squeeze('columns')
    dy = dy.squeeze('columns')
    dz = dz.squeeze('columns')
    # dx = hits.h[SPNAME].x.groupby(["entry", "chunk"]).first() - hits.h[SPNAME].x.groupby(["entry", "chunk"]).last()
    # dy = hits.h[SPNAME].y.groupby(["entry", "chunk"]).first() - hits.h[SPNAME].y.groupby(["entry", "chunk"]).last()
    # dz = hits.h[SPNAME].z.groupby(["entry", "chunk"]).first() - hits.h[SPNAME].z.groupby(["entry", "chunk"]).last()

    dr = np.sqrt(dx**2 + dy**2 + dz**2)
    dirx = dx / dr
    diry = dy / dr
    dirz = dz / dr

    outdf["dirx"] = dirx
    outdf["diry"] = diry
    outdf["dirz"] = dirz

    # dt along chunk
    # if NCHUNK > 1:
    #     dt = df.groupby(["entry", "chunk"])[[(hitsname, "h", "time", "")]].diff()
    #     dt.columns = ["dt"]
    #     dt = dt.join(df.chunk)
    #     dt = dt.groupby(["entry", "chunk"]).dt.mean()
    #     outdf = outdf.join(dt)
    # else:
    #     outdf["dt"] = np.nan
    
    # TPC/Cryo info
    outdf["tpcE"] = df.groupby(["entry", "chunk"]).tpcE.all()
    outdf["tpcW"] = (~outdf.tpcE) & (df.groupby(["entry", "chunk"]).tpcE.nunique() == 1)

    # Save T0
    outdf["pandora_t0"] = df.groupby(["entry", "chunk"]).t0PFP.first()
    outdf["hit_max_time_p2_tpcE"] = df.groupby(["entry", "chunk"]).hit_max_time_p2_tpcE.first()
    outdf["hit_max_time_p2_tpcW"] = df.groupby(["entry", "chunk"]).hit_max_time_p2_tpcW.first()

    # also save the cryostat number
    outdf["cryostat"] = df.groupby(["entry", "chunk"]).cryostat.first()
    # And run number
    outdf["run"] = df.groupby(["entry", "chunk"])[[('meta', 'run', '', ''),]].first()

    # Only save chunks that are all in one TPC
    outdf = outdf[outdf.tpcE | outdf.tpcW]
   
    return outdf


def main(output, inputs):
    b = plane2branches + branches.trkbranches
    if SAVEMC:
        b += truehitbranches

    ntuples = NTupleGlob(inputs, b)
    df = ntuples.dataframe(nproc="auto", f=reduce_df, concat="left")
    df.to_hdf(output, key="df", mode="w")

if __name__ == "__main__":
    # be nice
    os.nice(10) 

    printhelp = len(sys.argv) < 3 or sys.argv[1] == "-h"
    if printhelp:
        print("Usage: python make_etau_df.py [output.df] [inputs.root,]")
    else:
        main(sys.argv[1], sys.argv[2:])
