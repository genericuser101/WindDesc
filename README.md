# Descriptor-Based Surrogate Model of Wind Speeds in Offshore Wind Farms
![alt text](https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/1631825/wind-turbine-clipart-xl.png)

## Files:
### Data:
🖥️ Contains all the CSV files which are used to train the GP and ML models.

### Wind Desc:
* ⚙️ Cutoff - Contains the files for our cutoffs.
  
* ⚙️ Fingerprint_Calc - Contains the three descriptor model used to generate the fingerprints and neightbour lists for simulations.
  
* ⚙️ ML_Model - Machine Learning functionality and model.

* ⚙️ GP_Model - Gaussian Process functionality and active learning loops.
    * 📖 Windfarm_Active_Learning.ipynb    
    * 📖 Windfarm_Data_Vis.ipynb
    * 📖 Windfarm_New_Sim.ipynb
  
* ⚙️ Utils - Utility scripts for CSV handling, Active Learning, GP functionality and Data visualisation. 
    * 📜 AL_utility.py \
  AL_Helper (Responsible for Running Active Learning) 

    * 📜 CFD_utility.py \
  CFD_Helper (Responsible for Creating New zCFD Sims) 

    * 📜 CSV_Utility.py \
  CSV_Helper (Responsible for Extracting Data from Sims and Formatting) \
  CSV_Data_Vis (Responsible for Generating Interactive Data Representations) 

    * 📜 GP_utility.py \
  Turbine_Helper (Responsible for Parameter Assignment and Fingerprint Generation) \
  GP_Helper (Responsible for Training and Predicting using the GP model)

    * 📜 utilities.py \
  Complete utility classes, datalogging, messages, meta.

* ⚙️ zCFD_Import - Historic functionality and initial data merge.
