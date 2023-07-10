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

#Some formalities before we get to the best part
GP = GP_utility.GP_Helper()
TU = GP_utility.Turbine_Helper()
CFD = CFD_utility.CFD_Helper()
CSV = CSV_utility.CSV_Helper()

class AL_Helper():
    def __init__(self) -> None:
        pass
    
    #start_simnumber will be replaced with a funcation which looks at the last 
    def rock_and_roll(self, num_iter, filename, num_turb, tolerance, start_simnumber):  
        
        #1 Generate coords + Train Model
        turbines, neigh = CFD.generate_locations()
        trained_gp_model = GP.train_model(filename)

        refwind, refstdev = GP.predict_model(trained_gp_model, turbines, num_turb)
        
        #2 Check if model is happy
        if any(refstdev) > tolerance:
            #3 If happy cool, if sad run new simulation AKA ACTIVELY LEARN

            #4 Generate zCFD and run it 

            #5 Extract newly added data and throw in the desired data file
            
            #6 Retraing the model and see if happy now


            pass
        else:
            #Go to step 1
            pass 
