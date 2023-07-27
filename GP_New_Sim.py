from WD_Package import CFD_utility
from WD_Package import WD_config
config = WD_config.config()

CFD = CFD_utility.CFD_Helper(279.00, 4000.0, 500.0, 4)

turbines, neigh = CFD.generate_locations()

windspd = 10
winddir = 270

try:
    #sim_number = CFD.last_local_sim(config.simulations_path)
    sim_number = 6
    CFD.simulate(turbines, sim_number, windspd, winddir)
except FileExistsError:
    print("No simulation directory, should be neighbour to data, winddesc and mesh_creation!")