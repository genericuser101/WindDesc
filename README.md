# Descriptor-Based Surrogate Model of Wind Speeds in Offshore Wind Farms
![alt text](https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/1631825/wind-turbine-clipart-xl.png)

## Files:
### Data:
🖥️ Contains all the CSV files which are used to train the GP and ML models.

### Wind Desc:
* ⚙️ ML_Model - Machine Learning functionality and model.

* ⚙️ GP_Model - Gaussian Process functionality and active learning loops.
    * 📖 Windfarm_Active_Learning.ipynb    
    * 📖 Windfarm_Data_Vis.ipynb
    * 📖 Windfarm_New_Sim.ipynb
  
* ⚙️ WDPackage - Utility scripts for CSV handling, Active Learning, GP functionality and Data visualisation. 
    * 📜 AL_utility.py \
  AL_Helper (Responsible for Running Active Learning) 

    * 📜 CFD_utility.py \
  CFD_Helper (Responsible for Creating New zCFD Sims) 

    * 📜 CSV_Utility.py \
  CSV_Helper (Responsible for Extracting Data from Sims and Formatting) \
  CSV_Data_Vis (Responsible for Generating Interactive Data Representations) 

    * 📜 GP_utility.py \
  Turbine_Helper (Responsible for Parameter Assignment and Fingerprint Generation) \
  GP_Helper (Responsible for Training and Predicting using the GP model) \
  ❗ In the .predict_model() function the .predict() function calls from a GPy object, not model object ❗

    * 📜 utilities.py \
  Complete utility classes, datalogging, messages, meta.

    * 📜 cutoffs.py \
  Mathematical cutoffs and further functionality.

    * 📜 three_desc_model.py \
  Contains the three descriptor model used for predicting windspeeds.

### Active Learning: 
The active learning algorithm currently supports the following

### FAQ:
Q: I am parsing a the filename but, its returning a directory ValueError? \
A: If you aren't using the same architecture as WindDesc please pass the full path or at least the path from your code dir. Once the module is fully packaged the config file will be responsible for all this.

### Known Issues for submitting issues please email stefan.zhikharev@warwick.ac.uk:
0001 - All the pathing is hardcoded and stems from where the code is run, hence requires "../file" operators.
0002 - The imports require a path change, as the strucutre is not yet packaged together.

