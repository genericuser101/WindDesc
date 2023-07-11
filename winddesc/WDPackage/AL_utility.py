#If it were any smarter, it'd write a book, a book that would make Ulysses look like it was written in crayon.
#It would read it to you. This is my Eiffel Tower. This is my Rachmaninoff's Third. My Piéta. 
#It's completely elegant, it's bafflingly beautiful... - Justin Hummer @ Iron Man 2

#Call me Thanos the way I collect these utility files.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    
    #start_simnumber will be replaced with a funcation which looks at the last 
    def rock_and_roll(self, num_iter, filename, num_turb, tolerance, method):  
        
        folder_path = "home/eng/esugxk/storage/WindDesc/simulation"
        subfolders = os.listdir(folder_path)

        # Sort the subfolders in ascending order
        sorted_subfolders = sorted(subfolders, key=lambda x: int(x) if x.isdigit() else -1)

        # Get the last folder
        last_folder = sorted_subfolders[-1] if sorted_subfolders else None

        print("Value of the last folder:", last_folder)
        
        for i in range(num_iter):

            #Generate coords + Train Model
            turbines, neigh = self.CFD.generate_locations()
            trained_gp_model = self.GP.train_model(filename)
            refwind, refstdev = self.GP.predict_model(trained_gp_model, turbines, num_turb)

            if any(refstdev) > tolerance:

                #Training Fork for Methodologies
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
                
                #¬¬¬¬¬¬¬¬¬¬¬¬¬¬DO SIM NUMBER ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
                self.CFD.simulate(turbines, sim_number)
                
                #¬¬¬¬¬¬¬¬¬¬WE NEED TO WAIT FOR THE JOB TO BE DONE¬¬¬¬¬¬¬¬¬¬¬¬¬¬
                #Every 5 minutes check the existance of a file. 
                


                #5 Extract newly added data and throw in the desired data file
                
                #6 Retraing the model and see if happy now
                

                pass
            else:
                print("The model is happy, finding a new configuration.")
                pass 
