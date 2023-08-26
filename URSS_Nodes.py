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
CFD = CFD_utility.CFD_Helper(179.00, 4000.0, 500.0, 4)
CSV = CSV_utility.CSV_Helper()

data5 = np.array([[0., 0.],[1428.84921202,  -23.35385146],[200.92811144,   33.83056833],[ 302.2945072,  -134.25599054]])
data4 = np.array([[0.,0.], [ 493.69740653,  196.10550564], [1000.40201,      70.80528782], [1518.5244215 ,   74.73230136]])
data3 = np.array([[0. ,0. ], [ 350.5212639  ,  76.08606718], [ 770.9928804  , -62.04166999], [1935.13778969 , -77.57739242]])
data2 = np.array([[0.0,0.0],[ 694.36576595, -43.85822902], [ 449.31175435,  178.73675336], [1931.48005906 ,  71.47280391]])
data1 = np.array([[0.0,0.0],[ 794.36576595, 43.85822902], [ 449.31175435,  178.73675336], [2031.48005906 ,  71.47280391]])

data_array = np.array([data1, data2, data3, data4, data5])
certainty_array = []
stdev_arr = []
refwind_arr = []

num_turb = 4 
database = os.path.dirname(config.data_path)


for data in data_array:
    turbines = data
    for i in range(0,26,1):
        current_path = database + "/all_dataset_"+str(i)+".csv"
        CSV.new_format_to_old(current_path, current_path)

        trained_gp_model = GP.train_model(current_path)
        refwind, refstdev = GP.predict_model(trained_gp_model, turbines, num_turb)
        largest_err = max(refstdev)
        print("-----------------------------------------LARGEST-----------------------------------------")
        print(largest_err)

        print("STDEV:")
        print(refstdev)
        print("REFWIND")
        print(refwind)
        certainty_array.append(largest_err)
        stdev_arr.append(refstdev)
        refwind_arr.append(refwind)

        CSV.old_format_to_new(current_path, current_path)  

    print("-----------------------------------------FULL DATA-----------------------------------------")
    print(np.array(certainty_array))    
    print(np.array(stdev_arr))    
    print(np.array(refwind_arr))    

    certainty_array = []
    stdev_arr = []
    refwind_arr = []
