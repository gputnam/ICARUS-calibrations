source /cvmfs/icarus.opensciencegrid.org/products/icarus/setup_icarus.sh
setup python v3_9_2
setup hdf5 v1_12_0a -q e20:prof
. env/bin/activate
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/xrootd-5.5.1/build/lib64
