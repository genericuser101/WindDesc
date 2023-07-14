#If it were any smarter, it'd write a book, a book that would make Ulysses look like it was written in crayon.
#It would read it to you. This is my Eiffel Tower. This is my Rachmaninoff's Third. My Piéta. 
#It's completely elegant, it's bafflingly beautiful... - Justin Hummer @ Iron Man 2

#Call me Thanos the way I collect these utility files.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time 

import CFD_utility 
import GP_utility
import CSV_utility 


class AL_Helper():
    def __init__(self) -> None:
        #Some formalities before we get to the best part
        self.GP = GP_utility.GP_Helper()
        self.TU = GP_utility.Turbine_Helper()
        self.CFD = CFD_utility.CFD_Helper()
        self.CSV = CSV_utility.CSV_Helper()

    def last_local_sim(self, folder_path):

        subfolders = os.listdir(folder_path)

        # Sort the subfolders in ascending order
        sorted_subfolders = sorted(subfolders, key=lambda x: int(x) if x.isdigit() else -1)

        # Get the last folder
        local_sim_num = sorted_subfolders[-1] if sorted_subfolders else None

        return local_sim_num
    
    def rock_and_roll(self, num_iter, filename, num_turb, tolerance, method, windspeed):  

        local_sim_num = self.last_local_sim("../../simulation")
        local_sim_num += 1
        
        for i in range(num_iter):

            #Generate coords + Train Model
            turbines, neigh = self.CFD.generate_locations()
            trained_gp_model = self.GP.train_model(filename)
            refwind, refstdev = self.GP.predict_model(trained_gp_model, turbines, num_turb)

            #Check if there are any outliers in the tolerancing.
            if any(refstdev) > tolerance:

                #Training fork for the methodologies.
                try:
                    if method == "simple":
                        pass
                    elif method == "bayesian":
                        pass 
                    elif method == "autoencoder":
                        pass
                    #¬¬¬¬¬¬¬¬ADD MORE TECHNIQUES¬¬¬¬¬¬¬¬¬¬¬¬¬

                except ValueError:
                    print("Training method not recognised. Check github for currently supported.")
                
                #New simulation is run on the fed-forward coordinates.
                self.CFD.simulate(turbines, local_sim_num)
                
                #¬¬¬¬¬¬¬¬¬¬WE NEED TO WAIT FOR THE JOB TO BE DONE¬¬¬¬¬¬¬¬¬¬¬¬¬¬
                #Every 20 minutes check the existance of a file. 
                simFlag = False
                while simFlag == False:
                    simFlag = self.CFD.is_simulation_finished(local_sim_num)
                    time.sleep(1200)

                #Extract newly added data and throw in the desired data file.
                self.CSV.extract_turbine_data("../../data/all_Dataset_V2", num_turb, windspeed, local_sim_num)
                local_sim_num += 1

                #6 Retraing the model and see if happy now
                trained_gp_model = self.GP.train_model(filename)
                refwind, refstdev = self.GP.predict_model(trained_gp_model, turbines, num_turb)

            else:
                print("The model is happy, finding a new configuration.")
                 
