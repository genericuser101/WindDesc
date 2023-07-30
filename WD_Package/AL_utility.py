#If it were any smarter, it'd write a book, a book that would make Ulysses look like it was written in crayon.
#It would read it to you. This is my Eiffel Tower. This is my Rachmaninoff's Third. My Piéta. 
#It's completely elegant, it's bafflingly beautiful... - Justin Hummer @ Iron Man 2

#Call me Thanos the way I collect these utility files.
import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time 
from itertools import combinations

from WD_Package import WD_config
config = WD_config.config()

from WD_Package import CFD_utility 
from WD_Package import GP_utility
from WD_Package import CSV_utility 


class AL_Helper():
    def __init__(self) -> None:
        #Some formalities before we get to the best part
        self.GP = GP_utility.GP_Helper()
        self.TU = GP_utility.Turbine_Helper()
        self.CFD = CFD_utility.CFD_Helper()
        self.CSV = CSV_utility.CSV_Helper()
    
    def rock_and_roll(self, num_iter, num_turb, fine_tol, abs_tol, method, windspd, winddir):  
        
        local_sim_num = self.CFD.last_local_sim(config.simulations_path)
        local_sim_num += 1
        
        #------------------------------------TRAINING FORK-----------------------------------------#
        try:
            if method == "simple":
                encoder = simple_Encoder()
            elif method == "zhikh":
                encoder = zhikh_Encoder(fine_tol, abs_tol)
        except ValueError:
            print("Training method not recognised. Check github for currently supported.")

        #------------------------------------ITERATIVE LOOP----------------------------------------#
        for i in range(num_iter):

            print(f"Active learning iteration: {i}, started using the {method} encoder.")

            #Generate coords + Train Model
            turbines, neigh = self.CFD.generate_locations()
            trained_gp_model = self.GP.train_model(config.data_path)
            refwind, refstdev = self.GP.predict_model(trained_gp_model, turbines, num_turb)

            #Check if there are major errors.
            if any(refstdev) > abs_tol:
                
                encoder.project(refwind, refstdev, num_turb, turbines)

                #New simulation is run on the fed-forward coordinates.
                self.CFD.simulate(turbines, local_sim_num)
                
                #Every 20 minutes check the existance of a file. 
                simFlag = False
                while simFlag == False:
                    simFlag = self.CFD.is_sim_done(local_sim_num)
                    time.sleep(1200)

                #Extract newly added data and throw in the desired data file.
                self.CSV.extract_turbine_data(config.data_path, num_turb, windspd, local_sim_num)
                local_sim_num += 1

                #Retraing the model and see if happy now
                trained_gp_model = self.GP.train_model(config.data_path)
                refwind, refstdev = self.GP.predict_model(trained_gp_model, turbines, num_turb)

            else:
                print("The model is happy, finding a new configuration.")
                 

class simple_Encoder():
    def __init__(self) -> None:
        pass

    def project(self, refwind, refstdev, num_turb, positions):
        return positions
        

class zhikh_Encoder():
    def __init__(self, fine_tol, abs_tol) -> None:

        #------------------------Properties------------------------#
        self.fine_tol = fine_tol
        self.abs_tol = abs_tol

        #-------------------------Utilities------------------------#
        self.TU = GP_utility.Turbine_Helper()
        self.CSV = CSV_utility.CSV_Helper()

    def project(self, refwind, refstdev, num_turb, positions):

        fingerprints = self.TU.fingerprint(positions, num_turb)
        relevant_dataset = os.path.dirname(config.data_path) + "/" + num_turb + "_turbine_data.csv"
        num_meet_criterion = sum(1 for element in refstdev if element > self.abs_tol)

        #Case A: All errors are high.
        if all(error > self.abs_tol for error in refstdev):
            return positions 
        
        #Case B: More than half of errors high.
        if num_meet_criterion > len(refstdev) / 2:
            pass

        #Case C: Less than half of errors high.
        elif num_meet_criterion < len(refstdev) / 2:
            pass
    
    def small_errors_to_high(self):
        pass

    def small_errors_to_medium(self):
        pass 
    
    def get_X_closest(self, X, point):
        pass 

    def distance_to_point(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5