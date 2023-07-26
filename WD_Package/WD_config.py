import os

class config():
    def __init__(self) -> None:
        #Currently redundant but these dont take up too much space.
        self.simulations_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/simulation"     
        self.data_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_Dataset_V2.csv"  
        self.template_files_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/template"   
        self.mesh_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/Mesh_creation/"   

        #Unused PATH
        self.package_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/WD_Package" 

        self.initialize()

    def initialize(self):
        #get the current path of the script
        current_path = os.path.abspath(__file__)
        folder_path = os.path.dirname(current_path)
        
        files_in_folder = os.listdir(folder_path)

        config_filename = "config.txt"
        
        complete_config_path = os.path.join(folder_path, config_filename)

        #Makes sure file is present
        if config_filename in files_in_folder:
            #The file exsits.
            self.read_config(complete_config_path)
        else:
            #The file does not exist.
            #First we create the file.
            with open(complete_config_path, 'w'):
                pass
            self.select_paths(complete_config_path)
            

    def read_config(self, complete_config_path):
        with open(complete_config_path, 'r') as file:
            lines = file.readlines() 
            self.simulations_path = lines[0].strip()
            self.data_path = lines[1].strip()
            self.template_files_path = lines[2].strip()
            self.mesh_path = lines[3].strip()
            print("Config read OK.")


    def select_paths(self, complete_config_path):
        d_sim_path = input("Simulations Path: ")
        d_data_path = input("Data Path: ")
        d_temp_path = input("Template Path: ")
        d_mesh_path = input("Mesh Path: ")
        with open(complete_config_path, 'a') as file:
            file.write(d_sim_path + "\n")
            file.write(d_data_path + "\n")
            file.write(d_temp_path + "\n")
            file.write(d_mesh_path + "\n")
            print("Config write OK.")
        self.read_config(complete_config_path)

