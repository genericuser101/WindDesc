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

num_turb = 4 
database = os.path.dirname(config.data_path)
current_path = config.data_path

local_csv_file = "data_.csv"
turbines = np.array([[0.0,0.0],[ 794.36576595, 43.85822902], [ 449.31175435,  178.73675336], [2031.48005906 ,  71.47280391]])


CSV.new_format_to_old(current_path, current_path)
trained_gp_model = GP.train_model(current_path)
refwind, refstdev = GP.predict_model(trained_gp_model, turbines, num_turb)
largest_err = max(refstdev)
tail_array = np.vstack((refwind, refstdev))
print(tail_array)
print(np.shape(tail_array))
df_row = pd.DataFrame([tail_array])
existing_df = pd.read_csv(local_csv_file)
combined_df = pd.concat([existing_df, df_row], ignore_index=True)
combined_df.to_csv(local_csv_file, index=False)
CSV.old_format_to_new(current_path, current_path)  