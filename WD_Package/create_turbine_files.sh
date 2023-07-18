#!/bin/bash

#cd ..
#windir=270
#winspd=10
k=$1
numturb=$2
windspd=$3
winddir=$4
windirf=$windir.0
basecase="sim_${k}"
casename="${basecase}_${windir}p00_${winspd}p00"
mkdir simulation/$k
cp catalyst.py simulation/$k/catalyst.py
cp Siemens_SWT_2.3-93_106.5d_2.3MW_R93m_H63.3m_Air1.225.trbx simulation/$k/Siemens_SWT_2.3-93_106.5d_2.3MW_R93m_H63.3m_Air1.225.trbx
cp turbine.stl simulation/$k/turbine.stl
cp xy_turbine.txt simulation/$k/xy_turbine.txt
cp zcfd.lic simulation/$k/zcfd.lic
cp turbine.py simulation/$k/${basecase}.py
cp make_turbine_zones.py simulation/$k/make_turbine_zones.py
sed -i -e"s/basecase/${basecase}/" simulation/$k/make_turbine_zones.py
cp make_new_zones.py simulation/$k/make_new_zones.py
sed -i -e"s/basecase/${basecase}/" simulation/$k/make_new_zones.py
cp turbine.job simulation/$k/$k.job
sed -i -e "s/windir/$windir/g" -e "s/casename/$casename/" simulation/$k/$k.job
cp snappyHexMeshDict mesh_creation/system/snappyHexMeshDict
( #Subshell to return to correct directory
    cd mesh_creation 
    bash mesh_creation.sh
)
cp mesh_creation/zCFDInterface/Mesh_creation.h5 simulation/$k/turbine.h5
rm -rf mesh_creation/zCFDInterface
rm -rf 1
cd simulation/$k
echo sbatch $k.job
cd ../..
exit $exitcode
