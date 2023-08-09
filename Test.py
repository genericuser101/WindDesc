from WD_Package import CSV_utility 
from WD_Package import AL_utility
from WD_Package import WD_config
config = WD_config.config()     
from WD_Package import CFD_utility 

CFD = CFD_utility.CFD_Helper(279.00, 4000.0, 500.0, 4)
BigAL = AL_utility.AL_Helper()

turbines, neigh = CFD.generate_locations()

#BigAL.info_log(f"New Configuration: \n {turbines}" )

