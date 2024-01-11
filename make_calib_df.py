import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import datetime as dt
from lib.ntuple_glob import NTupleGlob
from lib import branches
import numpy as np
import os

os.nice(10)

# load constants
from lib.constants import *

PLANE = 2
SPNAME = "sp"

plane2branches = [
    "h.time", "h.width", "h.tpc", "h.channel", "h.wire", "dqdx", "pitch", "rr", "dir.x", "dir.y", "dir.z",
    "h.start", "h.end", "h.mult",
    "h.integral", "h.sumadc",
    "h.truth.e", "h.truth.nelec",
    "h.%s.x" % SPNAME, "h.%s.y" % SPNAME, "h.%s.z" % SPNAME,
]
plane2branches = ["hits%i.%s" % (PLANE, s) for s in plane2branches]

ray_branches = [
    "daughter_nsp",
    "daughter_pdg",
    "daughter_sp_toend_dist"
]

truebranches = [
  "truth.michel.genE",
  "truth.p.pdg",
]

truehitbranches = [
  "channel", "ndep", "nelec", "e", "rr", "pitch", "pitch_sce", "time", "p.x", "p.y", "p.z", "itraj", "tdrift",
  "p_scecorr_width.x", "p_scecorr_width.y", "p_scecorr_width.z"
]
truehitbranches = ["truth.p.truehits%i.%s" % (PLANE, s) for s in truehitbranches]

othrtrkbranches = [
  "tracks_near_start_dist",
  "tracks_near_start_costh"
]


t0 = 0
def exp(t, *p):
    A,tau = p
    return A*np.exp(-(t - t0)/tau)

def isTPCE(df):
    return df.tpc <= 1

def dist(df1, df2):
    return np.sqrt((df1.x-df2.x)**2 + (df1.y-df2.y)**2 + (df1.z-df2.z)**2)

def reduce_df(df, raydf=None, truehdf=None, othrdf=None):
    if df.empty:
        return None

    # Select stopping tracks
    select_track = (df.selected == 0) & (df.length > 50)

    hitname = "hits%i" % PLANE

    df["tpcE"] = isTPCE(df[hitname].h)

    df["true_end_dist"] = dist(df.end, df.truth.p.end)

    df["true_pdg"] = df.truth.p.pdg
    df["true_wallin"] = df.truth.p.wallin

    # df[("whicht0", "", "", "")] = -1

    # What to save
    outdf = df.loc[(df[hitname].dqdx > 0) & (df[hitname].rr < 300.) & select_track, 
                  [ (hitname, "h", "time", ""),
                    ("tpcE", "", "", ""),
                    (hitname, "h", "channel", ""),
                    (hitname, "h", "wire", ""),
                    ("true_pdg", "", "", ""),
                    ("true_wallin", "", "", ""),
                    ("true_end_dist", "", "", ""),
                    (hitname, "dqdx", "", ""),
                    (hitname, "pitch", "", ""),
                    (hitname, "rr", "", ""),
                    (hitname, "h", SPNAME, "x"),
                    (hitname, "h", SPNAME, "y"),
                    (hitname, "h", SPNAME, "z"),
                    (hitname, "dir", "x", ""),
                    (hitname, "dir", "y", ""),
                    (hitname, "dir", "z", ""),
                    (hitname, "h", "width", ""),
                    (hitname, "h", "start", ""),
                    (hitname, "h", "end", ""),
                    (hitname, "h", "mult", ""),
                    (hitname, "h", "integral", ""),
                    (hitname, "h", "sumadc", ""),
                    (hitname, "h", "truth", "e"),
                    (hitname, "h", "truth", "nelec"),
                    ("meta", "run", "", ""),
                    ("meta", "subrun", "", ""),
                    ("meta", "evt", "", ""),
                    ("cryostat", "", "", ""),
                    ("t0", "", "", ""),
                    #("whicht0", "", "", ""),
                    ("dir", "y", "", ""),
                    ("hit_min_time_p2_tpcE", "", "", ""),
                    ("hit_max_time_p2_tpcE", "", "", ""),
                    ("hit_min_time_p2_tpcW", "", "", ""),
                    ("hit_max_time_p2_tpcW", "", "", ""),
                    ("truth", "michel", "genE", ""),
                   ]
                  ].copy()

    # Simplify column names
    outdf.columns = ["time", "tpcE", "channel", "wire", "true_pdg", "true_wallin", "true_end_dist", "dqdx_nocorr", "pitch", "rr", "p_x", "p_y", "p_z", "dir_x", "dir_y", "dir_z", "width", "start", "end", "mult", "integral", "sumadc", "trueh_e", "trueh_nelec", "run", "subrun", "evt", "cryostat", "pandora_t0", 
    #"whicht0",
     "tdir_y", "mint_tpcE", "maxt_tpcE", "mint_tpcW", "maxt_tpcW", "michelE"]
    
    # Save information on PFP daughters
    if raydf is not None:
        closest_tdaughter = raydf.groupby(level=0).daughter_sp_toend_dist.min()
        outdf = outdf.join(closest_tdaughter.rename("closest_tdaughter"), on="entry", how="left")

    # Merge in true-hit information
    if truehdf is not None:
        truehdf = truehdf.truth.p["true" + hitname]
        truehdf.columns = ["true_" + "_".join(list(filter(lambda s: s, c))) for c in truehdf.columns] # pd.MultiIndex.from_tuples([("true_" + s, '', '', '') for s in truehdf.columns])
        outdf = outdf.reset_index().merge(truehdf, left_on=['entry', 'channel'],
                                      right_on=['entry', 'true_channel'],
                                      how="left", validate="many_to_one")

        outdf = outdf.set_index(["entry", "subentry"])

    if othrdf is not None and False:
        othrdf = othrdf.loc[othrdf.tracks_near_start_dist > 0, ["tracks_near_start_dist", "tracks_near_start_costh"]]

        closest_trk = othrdf.groupby(level=0).tracks_near_start_dist.idxmin()
        closest_othrdf = othrdf.loc[closest_trk].droplevel("subentry")
        outdf = outdf.join(closest_othrdf.tracks_near_start_dist.rename("closest_othr_trk_dist"), on="entry", how="left")
        outdf = outdf.join(closest_othrdf.tracks_near_start_costh.rename("closest_othr_trk_costh"), on="entry", how="left")

        aligned_trk = othrdf.groupby(level=0).tracks_near_start_costh.idxmax()
        aligned_othrdf = othrdf.loc[aligned_trk].droplevel("subentry")
        outdf = outdf.join(aligned_othrdf.tracks_near_start_dist.rename("aligned_othr_trk_dist"), on="entry", how="left")
        outdf = outdf.join(aligned_othrdf.tracks_near_start_costh.rename("aligned_othr_trk_costh"), on="entry", how="left")

    return outdf

def main(output, inputs):
    ntuples = NTupleGlob(inputs, branches.trkbranches + truebranches + plane2branches + ray_branches + truehitbranches) # + othrtrkbranches)
    df = ntuples.dataframe(nproc="auto", f=reduce_df)
    df.to_hdf(output, key="df", mode="w")

if __name__ == "__main__":
    printhelp = len(sys.argv) < 3 or sys.argv[1] == "-h"
    if printhelp:
        print("Usage: python make_calib_df.py [output.df] [inputs.root,]")
    else:
        main(sys.argv[1], sys.argv[2:])
