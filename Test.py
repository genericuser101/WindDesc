import WD_Package.WD_config as config1
import WD_Package.CSV_utility
config = config1.config()
CSV = WD_Package.CSV_utility.CSV_Helper()
CSV.split_data_by_turb([2, 3])
