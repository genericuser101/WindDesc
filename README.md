# Descriptor-Based Surrogate Model of Wind Speeds in Offshore Wind Farms

![alt text](https://w7.pngwing.com/pngs/683/243/png-transparent-wind-farm-energy-windmill-wind-power-energy-logo-industry-farm.png)

🚀turbine_files are the CFD outputs in .csv file format for 2 and 3 turbine simulations with 10 m/s. 

🚀cutoffs.py provides cutoff function for lateral and radial buffer zones for smoother transition.

🚀dataset_10m_s.csv is aggregated data file containing all CFD outputs.

🚀GP_surrogate_model.ipynb is a jupyter notebook file for training a GPR surrogate model using the dataset_10m_s.csv.

🚀parameter_optimisation.ipynb is jupyter notebook file for minimising error rate with changing parameters of descriptors.

🚀three_desc_model.py is main function that converts turbine locations to fingerprints with 3 descriptors.

🚀utilities.py privides auxiliary functions.
