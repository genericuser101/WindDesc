# Descriptor-Based Surrogate Model of Wind Speeds in Offshore Wind Farms
![alt text](https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/1631825/wind-turbine-clipart-xl.png)

## Files:
### Data:
🖥️ Contains all the CSV files which are used to train the GP and ML models.

### Wind Desc:
⚙️ Cutoff - Contains the files for our cutoffs. \
⚙️ Fingerprint_Calc - Contains the three descriptor model used to generate the fingerprints for simulations. \
⚙️ Ml_Model - Machine Learning functionality and model. \
⚙️ Utils - Utility scripts for CSV handling, Active Learning, GP functionality and Data visualisation. \
    📜 AL_utility: AL_Helper (Responsible for Running Active Learning) \
    📜 CFD_utility: CFD_Helper (Responsible for Creating New zCFD Sims) \
    📜 CSV_Utility: CSV_Helper (Responsible for Extracting Data from Sims and Formatting) \
                    CSV_Data_Vis (Responsible for Generating Interactive Data Representations) \
    📜 GP_utility: Turbine_Helper (Responsible for Parameter Assignment and Fingerprint Generation) \
                    GP_Helper (Responsible for Training and Predicting using the GP model) \
⚙️ zCFD_Import - Historic functionality and initial data merge.
