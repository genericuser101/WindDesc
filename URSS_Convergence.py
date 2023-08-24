import os
import math
from typing import Any
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time 
from itertools import combinations
import csv 
import datetime

from WD_Package import WD_config
config = WD_config.config()

from WD_Package import CFD_utility 
from WD_Package import GP_utility 
from WD_Package import CSV_utility 

GP = GP_utility.GP_Helper()
TU = GP_utility.Turbine_Helper()
CFD = CFD_utility.CFD_Helper(279.00, 4000.0, 500.0, 4)
CSV = CSV_utility.CSV_Helper()
 
database = os.path.dirname(config.data_path)

certainty_array = []

num_turb = 4 

#Data 1
#turbines=np.array([[0.0,0.0],[ 794.36576595, 43.85822902], [ 449.31175435,  178.73675336], [2031.48005906 ,  71.47280391]])

#Data 2
turbines=np.array([[0.0,0.0],[ 694.36576595, -43.85822902], [ 449.31175435,  178.73675336], [1931.48005906 ,  71.47280391]])




print("Final Locations:")
print(turbines)

for i in range(0,26,1):
    current_path = database + "/all_dataset_"+str(i)+".csv"
    CSV.new_format_to_old(current_path, current_path)

    trained_gp_model = GP.train_model(current_path)
    refwind, refstdev = GP.predict_model(trained_gp_model, turbines, num_turb)
    largest_err = max(refstdev)
    print("----------------LARGEST----------------")
    print(largest_err)

    print("STDEV:")
    print(refstdev)
    certainty_array.append(largest_err)
    CSV.old_format_to_new(current_path, current_path)  

text_file = "URSS_log.txt"

print("Stdev Array")
print(np.array(certainty_array))           


