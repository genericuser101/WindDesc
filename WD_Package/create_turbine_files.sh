#!/bin/bash

#cd ..
#windir=270
#winspd=10
k=$1
numturb=$2
windspd=$3
winddir=$4
temppath=$5
simpath=$6
meshpath=$7
windirf=$windir.0
basecase="sim_${k}"
casename="${basecase}_${windir}p00_${winspd}p00"
mkdir $simpath/$k
cp $temppath/catalyst.py $simpath/$k/catalyst.py
cp $temppath/Siemens_SWT_2.3-93_106.5d_2.3MW_R93m_H63.3m_Air1.225.trbx $simpath/$k/Siemens_SWT_2.3-93_106.5d_2.3MW_R93m_H63.3m_Air1.225.trbx
cp $temppath/turbine.stl $simpath/$k/turbine.stl
cp $temppath/xy_turbine.txt $simpath/$k/xy_turbine.txt
cp $temppath/zcfd.lic $simpath/$k/zcfd.lic
cp $temppath/turbine.py $simpath/$k/${basecase}.py
cp $temppath/make_turbine_zones.py $simpath/$k/make_turbine_zones.py
sed -i -e"s/basecase/${basecase}/" $simpath/$k/make_turbine_zones.py
cp $temppath/make_new_zones.py $simpath/$k/make_new_zones.py
sed -i -e"s/basecase/${basecase}/" $simpath/$k/make_new_zones.py
cp $temppath/turbine.job $simpath/$k/$k.job
sed -i -e "s/windir/$windir/g" -e "s/casename/$casename/" $simpath/$k/$k.job
cp $temppath/snappyHexMeshDict $meshpath/system/snappyHexMeshDict
( #We execute the mesh file but also pass it the meshpath command because $PWD returns
  #the path from where the script is envoked. 
    rm -rf $meshpath/zCFDInterface
    rm -rf $meshpath/1
    bash $meshpath/mesh_creation.sh $meshpath
)
cp $meshpath/zCFDInterface/Mesh_creation.h5 $simpath/$k/turbine.h5
echo sbatch $simpath/$k/$k.job
#Run the job, selection for exitcode = 0, greenlight, else, manual interferance
exit $exitcode
