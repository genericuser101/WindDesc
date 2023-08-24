from WD_Package import CSV_utility 
from WD_Package import AL_utility
from WD_Package import WD_config
config = WD_config.config()     
from WD_Package import CFD_utility 
from WD_Package import GP_utility
import os 

GP = GP_utility.GP_Helper()
CFD = CFD_utility.CFD_Helper(279.00, 4000.0, 500.0, 4)

turbines, neigh = CFD.generate_locations()

#BigAL.info_log(f"New Configuration: \n {turbines}" )

num_turb = 4

CSV = CSV_utility.CSV_Helper()
database = os.path.dirname(config.data_path)
current_path = database + "/all_dataset_0.csv"

trained_gp_model = GP.train_model(current_path)
refwind, refstdev = GP.predict_model(trained_gp_model, turbines, num_turb)
print(refwind)
print(refstdev)
