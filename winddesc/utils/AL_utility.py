#If it were any smarter, it'd write a book, a book that would make Ulysses look like it was written in crayon.
#It would read it to you. This is my Eiffel Tower. This is my Rachmaninoff's Third. My Piéta. 
#It's completely elegant, it's bafflingly beautiful... - Justin Hummer @ Iron Man 2

#Call me Thanos the way I collect these utility files.
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
    def rock_and_roll(self, num_iter, filename, num_turb, tolerance, start_simnumber, method):  
        
        #insert code for the last file value in the sim dir.
        
        for i in range(num_iter):

            #Generate coords + Train Model
            turbines, neigh = self.CFD.generate_locations()
            trained_gp_model = self.GP.train_model(filename)
            refwind, refstdev = self.GP.predict_model(trained_gp_model, turbines, num_turb)

            if any(refstdev) > tolerance:

                #Training Fork
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
                
                self.C 




                #5 Extract newly added data and throw in the desired data file
                
                #6 Retraing the model and see if happy now
                

                pass
            else:
                print("The model is happy, finding a new configuration.")
                pass 
