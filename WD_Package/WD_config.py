class config():
    def __init__(self) -> None:
        #The PATH is structured from where you are calling the functions.
        self.simulations_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/simulation"             #ENTER SIMULATION PATH
        self.data_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/data/all_Dataset_V2.csv"       #ENTER DATA.CSV PATH
        self.template_files_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/template"            #ENTER WHERE YOU WANT TEMPLATE TO STORE
        self.mesh_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/Mesh_creation"                 #ENTER WHERE MESH IS MADE
        self.package_path = "/home/eng/esugxk/storage/WindDesc/WindDesc/WD_Package"