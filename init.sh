#!/bin/bash 
source /cvmfs/larsoft.opensciencegrid.org/spack-v0.22.0-fermi/setup-env.sh
spack load hdf5@1.14.3%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3
spack load xrootd@5.6.9%gcc@12.2.0

python -m venv env
. env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd landau
python setup.py install --prefix=$VIRTUAL_ENV
cd ..
