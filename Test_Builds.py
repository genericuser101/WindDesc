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
current_path = str(database) + "/all_dataset_0.csv"
print(current_path)
for i in range(10):
    turbines, neigh = CFD.generate_locations()

    CSV.new_format_to_old(current_path, current_path)
    trained_gp_model = GP.train_model(current_path)
    refwind, refstdev = GP.predict_model(trained_gp_model, turbines, num_turb)
    fingerprint = TU.fingerprint(turbines, num_turb)
    largest_err = max(refstdev)
    [refwind2, referr] = trained_gp_model.predict(fingerprint)
    CSV.old_format_to_new(current_path, current_path) 
    if largest_err > 0.5:
        print("-----------------------------------------Found-----------------------------------------")
        print(turbines)
        break
print(refwind)
print(refstdev)
print(referr)
print("DONE")