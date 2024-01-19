source /cvmfs/icarus.opensciencegrid.org/products/icarus/setup_icarus.sh
setup python v3_9_2
setup hdf5 v1_12_0a -q e20:prof
python -m venv env
. env/bin/activate
pip install -r requirements.txt
echo INSTALLING LANDAU PACKAGE
cd landau
python setup.py install --prefix=$VIRTUAL_ENV
cd ..
echo DOWNLOADING AND INSTALLING XROOTD
wget http://xrootd.org/download/v5.5.1/xrootd-5.5.1.tar.gz
tar -xvzf xrootd-5.5.1.tar.gz 
rm xrootd-5.5.1.tar.gz
cd xrootd-5.5.1/
mkdir build
cd build
ln -s /cvmfs/larsoft.opensciencegrid.org/products/cmake/v3_22_2/Linux64bit+3.10-2.17/bin/cmake cmake3
export PATH=$PATH:$PWD
mkdir lib64
cmake3 .. -DCMAKE_INSTALL_PREFIX=$PWD
make install -j 16
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/lib64
cd bindings/python
python setup.py install --prefix=$VIRTUAL_ENV
cd ../../../..
