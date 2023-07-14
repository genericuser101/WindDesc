#This script contains the funcationality for everything that requires to run a new CFD simulation.
#Main imports
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

#Required Files
from cutoffs import Polynomial
import GP_utility as GP
import three_desc_model as exponential_new


class CFD_Helper():


    def __init__(self, min_dist, max_xdist, max_ydist, num_turb) -> None:
        self.min_dist = min_dist
        self.max_xdist = max_xdist
        self.max_ydist = max_ydist
        self.num_turb = num_turb
        self.turbine_utility = GP.Turbine_Helper()
        self.nl = self.turbine_utility.nl
        self.turb = [self.turbine_utility.symbol]


    #Jingjing's random turbine generation.
    def generate_locations(self):
        while True:
            # Generate random coordinates
            turbines = np.zeros([self.num_turb,2])
            for i in range(1,self.num_turb):
                # X coordinate from triangular distribution (mode 0)
                turbines[i,0]=np.random.triangular(0,0,self.max_xdist)
                # y coordinate from triangular distribution (mode 0)
                turbines[i,1]=np.random.triangular(-self.max_ydist,0,self.max_ydist)
            print(f"Positions:\n {turbines}")
            neigh=self.nl.calculate(self.turb*self.num_turb,turbines) # And here
            print(f"Neighbour List: {neigh}")
            # Check neighbours
            for i in range(self.num_turb):
                if (len(neigh[i])==self.num_turb-1):
                    # if one of them has maximal number of neigbours: break loop
                    break
            else:
                # If none of them has maximal number of neighbours: Try again
                print("Not enough neighbours")
                continue
            # Check distances
            for i, j in combinations(range(self.num_turb), 2):
                if (np.linalg.norm(turbines[i]-turbines[j])<self.min_dist):
                    # Two turbines are too close
                    print("Distance between turbine ",i+1," and turbine ",j+1," is too low.")
                    break
            else:
                # None of the turbines are too close: SUCCESS!
                print("Configuration Found!")
                break
            continue

        return turbines, neigh 

    #Slightly modified version of Jingjings, simulate function. I actually dont know if she wrote this. 
    #Who cares no-one reads the comments longer than one line la la la windfarm goes brrrrr...
    def simulate(self, turbines, sim_number):
        positions = np.array(turbines)
        
        # Calculate distances between all pairs of turbines
        for i, j in combinations(range(self.num_turb), 2):
            if (np.linalg.norm(positions[i]-positions[j])<self.min_dist):
                print("Distance between turbine ",i+1," and turbine ",j+1," is too low")
                return -1
        
        # Generate turbine and cylinder coordinates based on position
        turbine_coords = [np.array([(positions[i][0]-2000),(positions[i][1])]) for i in range(self.num_turb)]
        cylinder_coords = [np.array([(positions[i][0]-2100),(positions[i][1])]) for i in range(self.num_turb)]
        
        # Generate hexmeshdict file
        # Part 1: Preamble
        data = '''/*--------------------------------*- C++ -*----------------------------------*\ 
    | =========                 |                                                 |
    | \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
    |  \\    /   O peration     | Version:  4.x                                   |
    |   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
    |    \\/     M anipulation  |                                                 |
    \*---------------------------------------------------------------------------*/
    FoamFile
    {
        version     2.0;
        format      ascii;
        class       dictionary;
        object      snappyHexMeshDict;
    }
    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
    castellatedMesh true;
    snap false;
    addLayers false;
    // https://sites.google.com/site/snappywiki/snappyhexmesh/snappyhexmeshdict/user-defined-regions
    geometry
    {
    '''
        # Part 2: Cylinders and spheres
        for i in range(self.num_turb):
            # 2a: Cylinder
            data = data + '''refinementCylinder{n}            
    {{
    type searchableCylinder;
    point1 ({cy1_x} {tcoord_y} 63.3);
    point2 ({cy2_x} {tcoord_y} 63.3);
    radius 80.0;
    }}
    '''.format(n=i,cy1_x=cylinder_coords[i][0],tcoord_y=turbine_coords[i][1],cy2_x=cylinder_coords[i][1])
            # 2b: Sphere
            data = data + ''' refinementSphere{} 
    {{
    type searchableSphere;
    centre ({} {} 63.3);
    radius 63.3;
    }}
    '''.format(i,turbine_coords[i][0],turbine_coords[i][1])
            
        # Part 3: Middle section
        data = data + '''
    };
    castellatedMeshControls
    {
    maxLocalCells 100000;
    maxGlobalCells 10000000;
    minRefinementCells 10;
    nCellsBetweenLevels 1;
    resolveFeatureAngle 30;
    features (); 
    refinementSurfaces { };
    refinementRegions
    {
    '''
        # Part 4: Cylinder/sphere settings
        for i in range(self.num_turb):
            data = data + '''refinementCylinder{n} 
    {{
    mode inside;
    levels ((1.0 1)); // one level of general refinement
    levelIncrement (0 1 (2 2 0)); // apply two level of refinement to any level 0 cells in the x and y directions only
    }}
    refinementSphere{n}
    {{
    mode inside;
    levels ((1.0 0));
    levelIncrement (0 3 (4 4 0)); // apply extra levels of directional refinement inside fine sphere.
    }}
    '''.format(n=i)
            
        # Part 5: End
        data = data +'''}
    locationInMesh (0.0 0.0 63.3);
    allowFreeStandingZoneFaces true;
    }
    meshQualityControls
    {
    maxNonOrtho 65;
    maxBoundarySkewness 20;
    maxInternalSkewness 4;
    maxConcave 80;
    minFlatness 0.5;
    minTetQuality 1e-30;
    minVol 1e-13;
    minArea -1;
    minTwist 0.05;
    minDeterminant 0.001;
    minFaceWeight 0.05;
    minVolRatio 0.01;
    minTriangleTwist -1;
    nSmoothScale 4;
    errorReduction 0.75;
    relaxed
    {
    maxNonOrtho 75;
    }
    nSmoothScale 4;
    errorReduction 0.75;
    }
    snapControls
    {
    nSmoothPatch 3;
    tolerance 2.0;
    nSolveIter 30;
    nRelaxIter 5;
    }
    addLayersControls
    {
    }
    mergeTolerance 1e-6;
    '''
        with open(r'snappyHexMeshDict', 'w') as file:
            file.write(data)

        #Write turbine file
        data=''
        for i in range(self.num_turb):
            data = data + 'T{:03d} {} {}\n'.format(i,str(turbine_coords[i][0]),str(turbine_coords[i][1]))
        with open(r'xy_turbine.txt', 'w') as file:
            file.write(data)
                #execute script for creating and submitting CFD simulation
        exit_code = os.system('bash create_turbine_files_3_turbine.sh '+str(sim_number).zfill(4)+' '+str(self.num_turb).zfill(2))
        print(exit_code)
            
        return 0

    def display_turbine_configuration(self, turbines):
        #Now that I changed the structure the try and catch kinda useless.
        try:
            _ = turbines.shape[0]
            # Rainbow colormap with as many colors as turbines
            cmap = plt.get_cmap('rainbow', _)

            # Plot turbines
            for i in range(_):
                plt.scatter(turbines[i,0], turbines[i,1], color=cmap(i), label='Turbine ' + str(i))

            # Set the desired limits for the x and yaxes
            plt.xlim(-300, 4500)
            plt.ylim(-500, 500)
            plt.axis('equal')

            # Add labels to each point
            for i in range(_):
                plt.text(turbines[i, 0], turbines[i, 1], str(i))

            # Add legends
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.title("Turbine Configuration")
            plt.show()

        except ValueError:
            print("!No Turbine Loctaions Generated!")
            print("Please run the .generate_locations() function.")


    def is_simulation_finished(self, sim_num):
        
        #First build the filepath
        filepath = "../../simulation/" + str(sim_num) + "/X-OUTPUT-FOLDER/LOGGING/file.log"

        with open(filepath, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode()
        
        if last_line == "Solver loop finished":
            return True
        else:
            return False
