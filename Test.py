import WD_Package.CSV_utility
import WD_Package.AL_utility
#CSV = WD_Package.CSV_utility.CSV_Helper()
from WD_Package import WD_config
config = WD_config.config()     
import WD_Package.CFD_utility
#CFD = WD_Package.CFD_utility.CFD_Helper(279.00, 4000.0, 500.0, 4)
#print(int(CFD.last_local_sim(config.simulations_path)) + 1 )
#CSV.old_format_to_new("/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset.csv", "/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset_SZ.csv")
#CSV.organise_data()
#its currently in the new format
#CSV.old_format_to_new("/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset_SZ.csv","/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset_SZ.csv")
#CSV.extract_turbine_data(config.data_path, 4, 10, 270, 4) 
#CSV.old_format_to_new("/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset_SZ.csv","/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset_SZ.csv")

BigAL = WD_Package.AL_utility.AL_Helper()
BigAL.rock_and_roll(1, 4, 0.01, 0.01, "simple", 10, 270)
