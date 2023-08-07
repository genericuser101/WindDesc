import WD_Package.CSV_utility
CSV = WD_Package.CSV_utility.CSV_Helper()
from WD_Package import WD_config
config = WD_config.config()     
#CSV.old_format_to_new("/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset.csv", "/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_dataset_SZ.csv")
#CSV.organise_data()
CSV.extract_turbine_data(config.data_path, 4, 10, 270, 4) 
