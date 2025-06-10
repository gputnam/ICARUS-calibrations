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

SPNAME = "sp"

plane2branches = [
    "h.time", "h.%s.y" % SPNAME, "h.%s.z" % SPNAME, "h.tpc", "oncalo"
]
plane2branches = ["hits2.%s" % s for s in plane2branches]

def isTPCE(df):
    return df.tpc <= 1

def reduce_df(df):
    def pad(b, npad):
        while len(b) < npad:
            b.append("")
        return tuple(b)

    # first make sure we save the per-track branches
    outdf = df[[pad(b.split("."), df.columns.nlevels) for b in branches.trkbranches]].groupby(level=0).first()

    # Recompute the per TPC min/max and also save other information for the min/max time hits

    # get the TPC thingy
    df["tpcE"] = isTPCE(df.hits2.h)
    
    # First -- only work with hits on the calo
    df = df[df.hits2.oncalo]

    # And separate the df into TPC E, W
    dfE = df[df.tpcE]
    dfW = df[~df.tpcE]

    # Same the time and the y and z points
    tosave = plane2branches[:3]
    tosave = [pad((b).split("."), df.columns.nlevels) for b in tosave]

    # Group by that and get the min, rows and max rows
    tpcE_min = dfE.loc[dfE.hits2.h.time.groupby(level=0).idxmin(), tosave].droplevel(1)
    tpcE_max = dfE.loc[dfE.hits2.h.time.groupby(level=0).idxmax(), tosave].droplevel(1)

    tpcW_min = dfW.loc[dfW.hits2.h.time.groupby(level=0).idxmin(), tosave].droplevel(1)
    tpcW_max = dfW.loc[dfW.hits2.h.time.groupby(level=0).idxmax(), tosave].droplevel(1)

    # Simplify column names
    colnames = ["time", "y", "z"]

    tpcE_min.columns = pd.MultiIndex.from_tuples([pad(["tpcE_min", b], outdf.columns.nlevels) for b in colnames]) 
    tpcE_max.columns = pd.MultiIndex.from_tuples([pad(["tpcE_max", b], outdf.columns.nlevels) for b in colnames]) 
    tpcW_min.columns = pd.MultiIndex.from_tuples([pad(["tpcW_min", b], outdf.columns.nlevels) for b in colnames]) 
    tpcW_max.columns = pd.MultiIndex.from_tuples([pad(["tpcW_max", b], outdf.columns.nlevels) for b in colnames]) 

    # Also -- save the time difference between hits for the largest and smallest times
    tpcE_max_10_dt = dfE.hits2.h.time.groupby(level=0).nlargest(10, keep="all").groupby(level=0).diff(-1).groupby(level=0).mean()
    tpcE_min_10_dt = dfE.hits2.h.time.groupby(level=0).nsmallest(10, keep="all").groupby(level=0).diff().groupby(level=0).mean()

    tpcW_max_10_dt = dfW.hits2.h.time.groupby(level=0).nlargest(10, keep="all").groupby(level=0).diff(-1).groupby(level=0).mean()
    tpcW_min_10_dt = dfW.hits2.h.time.groupby(level=0).nsmallest(10, keep="all").groupby(level=0).diff().groupby(level=0).mean()

    tpcE_max_10_dt.name = pad(["tpcE_max", "dt"], outdf.columns.nlevels)
    tpcE_min_10_dt.name = pad(["tpcE_min", "dt"], outdf.columns.nlevels)
    tpcW_max_10_dt.name = pad(["tpcW_max", "dt"], outdf.columns.nlevels)
    tpcW_min_10_dt.name = pad(["tpcW_min", "dt"], outdf.columns.nlevels)

    # Save
    outdf = outdf.join(tpcE_min)
    outdf = outdf.join(tpcE_min_10_dt)
    outdf = outdf.join(tpcE_max)
    outdf = outdf.join(tpcE_max_10_dt)
    outdf = outdf.join(tpcW_min)
    outdf = outdf.join(tpcW_min_10_dt)
    outdf = outdf.join(tpcW_max)
    outdf = outdf.join(tpcW_max_10_dt)

    return outdf

def main(output, inputs):
    ntuples = NTupleGlob(inputs, plane2branches + branches.trkbranches)
    df = ntuples.dataframe(nproc="auto", f=reduce_df, savemeta=True, concat="left")
    df.to_hdf(output, key="df", mode="w")

if __name__ == "__main__":
    printhelp = len(sys.argv) < 3 or sys.argv[1] == "-h"
    if printhelp:
        print("Usage: python make_driftV_adv_df.py [output.df] [inputs.root,]")
    else:
        main(sys.argv[1], sys.argv[2:])
