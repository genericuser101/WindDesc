#Call me Thanos the way I collect these utility files.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import CFD_utility 
import GP_utility
import CSV_utility 

folder_path = "home/eng/esugxk/storage/WindDesc/simulation"
subfolders = os.listdir(folder_path)

# Sort the subfolders in ascending order
sorted_subfolders = sorted(subfolders, key=lambda x: int(x) if x.isdigit() else -1)

# Get the last folder
last_folder = sorted_subfolders[-1] if sorted_subfolders else None

print("Value of the last folder:", last_folder)