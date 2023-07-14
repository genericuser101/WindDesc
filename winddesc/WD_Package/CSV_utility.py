#This script is responsible the CSV file manipulation and data visualisation

# importing required libraries
from mpl_toolkits.mplot3d import Axes3D

#Required Imports
import csv
import os
import GPy
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

from WD_Package import GP_utility
from WD_Package import WD_config
config = WD_config.config() 

from IPython.display import display
GPy.plotting.change_plotting_library('matplotlib')

class CSV_Helper():
    def __init__(self) -> None:
        pass
    
    #Written by Dr. Brommer and Jingjing, updated by Stef
    def extract_turbine_data(self, filename, num_turbs, windspeed, sim_num):
        
        #This gets us the local directory.
        simulation_directory=config.simulations_path+sim_num
        coordinate_file=simulation_directory+"/xy_turbine.txt"
        
        #Read coordinate file
        positions=pd.DataFrame()
        pos=pd.read_csv(coordinate_file, sep=' ',header=None)
        print(pos)

        #This uses a local filename, which is a checker rather than the filename parsed into function
        cfd_data=np.zeros(num_turbs)
        for filename_local in os.listdir(simulation_directory):
            if filename_local.endswith('.csv'):  # Only consider CSV files
                df=pd.read_csv(filename_local, sep=' ')
                df=df.tail(1) # Last line is the final result
                for i in range(0,num_turbs):
                    uref='T00%d_uref' %(i)
                    cfd_data[i]=df[uref].iloc[-1]
                print(cfd_data)

        #How many sims of the type.
        global_sim_num = self.get_last_sim(filename, num_turbs)
        global_sim_num = str(global_sim_num)

        #Finally the string is in a format such as 0000X or 00XXX, its zfill
        try:
            global_sim_num = global_sim_num.zfill(4)
        except ValueError:
            print("Oop at 10k sims, tell Stef to change code.")

        #¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬NEW NAMING FORMAT¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
        simname=global_sim_num+"_"+str(windspeed)+"_"+str(num_turbs)
        #Add directionality maybe
        #¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬

        dataset=pd.DataFrame()
        for i in range(num_turbs):
            turb_data=pd.DataFrame(
                [[pos[1].iloc[i]+2000, pos[2].iloc[i], cfd_data[i], num_turbs, simname,   i]], 
                columns=["X_coord",    "Y_coord",     "Ref_wind", "Num_tot_turb", "ID", "Turb_num"])
        #        [[pos[1].iloc[i]+2000,pos[2].iloc[i],cfd_data[i],windspeed,i,numturb, simname]], 
        #        columns=["x_coord", "y_coord", "ref_wind_speed","wind_speed" , "turb_num","num_tot_turb", "ID"])
            dataset = pd.concat([dataset, turb_data])

        dataset

        turbine_csv=pd.read_csv(filename,index_col=False)
        #turbine_csv=turbine_csv.drop(turbine_csv.columns[[0]],axis=1)
        turbine_csv = pd.concat([turbine_csv,dataset])
        turbine_csv = turbine_csv.reset_index(drop=True)

        print(turbine_csv)

        turbine_csv.to_csv(filename,index=True)

    def get_last_sim(self, filename, num_turbs):
        with open(filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            line_count = 0

            sim_count = 0

            for row in csv_reader:
                if line_count > 0:
                    if int(row[3]) == num_turbs:
                        sim_count += 1 
                line_count += 1

            sim_count = sim_count/3

        return int(sim_count)

    def sort_array_ascendX(self, arr):
        #Simple bubble sort for tuple arrays.
        #I solemly swear I wrote this code.
        array = arr
        n = len(array)
        
        #Traverse through all array elements
        for i in range(n):
            #Last i elements are already in place
            for j in range(0, n-i-1):
                #Swap if the element found is greater than the next element
                if array[j,0] > array[j+1,0]:
                    #If x greater then swap both coords
                    array[j,0], array[j+1,0] = array[j+1,0], array[j,0]
                    array[j,1], array[j+1,1] = array[j+1,1], array[j,1]
                
        #Return sorted array.
        return array

    def old_format_to_new(self, old_filename, new_filename):
        #Please update this function if the format changes and change the value in the comment below.
        #Current Format Version = 2

        input_file = old_filename
        output_file = new_filename

        with open(input_file, 'r') as file:
            csv_reader = csv.reader(file)
            rows = [row[1:] for row in csv_reader]  # Exclude the first column

        with open(output_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

        print(f"Modified CSV file saved as '{output_file}'.")


class CSV_Data_Vis():
    def __init__(self, filename) -> None:
        self.filename = filename

        self.helper = CSV_Helper()

    def display_2T_data(self):
        #First we will do 2 turbine models and further down move onto 3.
        dos_turb_Flag = True

        #Creates a figure to which we can plot the data.
        fig_2t = plt.figure()
        ax_2t = fig_2t.add_subplot(111)

        #Fancy looking legend, I dont know how to do it simpler, if you wanna edit, be my guest.
        legend_elements_2t = [Line2D([0], [0], marker='o', color='w', label = "Turbine 0",
                                markerfacecolor='brown'),
                            Line2D([0], [0], marker='o', color='w', label = "Turbine 1",
                                markerfacecolor='burlywood')]

        with open(self.filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            line_count = 0

        #In each row the loop checks if we are still in the 2 turbine area and then extracts the coordinates.
            for row in csv_reader:
                if line_count > 0:
                    num_turb = int(row[3])
                    if num_turb > 2:
                        dos_turb_Flag = False
                    else:
                        if dos_turb_Flag:
                            temp_x = float(row[0])
                            temp_y = float(row[1])
                            turb_val = float(row[5])
                            if turb_val == 0:
                                plt.scatter(temp_x, temp_y,color = "brown", marker="o", alpha=0.2)
                            elif turb_val == 1:
                                plt.scatter(temp_x, temp_y, color = "burlywood", marker="o", alpha=0.2)
                        else:
                            break
                line_count += 1

        ax_2t.set(title="Two Turbine Data Distribution")
        ax_2t.legend(handles=legend_elements_2t, loc="upper right")
        plt.show()

    def display_3T_data(self):
        #Creates a figure and its component axis to which we can plot the data.
        fig_3t = plt.figure()
        fig_3t1 = plt.figure()
        fig_3t2 = plt.figure()

        ax_3t = fig_3t.add_subplot(111)
        ax_3t1 = fig_3t1.add_subplot(111)
        ax_3t2 = fig_3t2.add_subplot(111)


        #Fancy looking legend, I dont know how to do it simpler, if you wanna edit, be my guest.
        legend_elements_3t = [Line2D([0], [0], marker='o', color='w', label = "Turbine 0",
                                markerfacecolor='brown'),
                            Line2D([0], [0], marker='o', color='w', label = "Turbine 1",
                                markerfacecolor='burlywood'),
                            Line2D([0], [0], marker='o', color='w', label = "Turbine 2",
                                markerfacecolor='powderblue'),
                                ]

        with open(self.filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            line_count = 0

            count = 0

            wind_path_array = np.array([[0., 0.], [0., 0.], [0.,0.]])

        #In each row the loop checks if we are still in the 3 turbine area and then extracts the coordinates.
            for row in csv_reader:
                if line_count > 0:
                    num_turb = int(row[3])
                    if num_turb == 3:
                            #Since starts at 0, does on the 4th.
                            if count % 3 == 0:
                                #Reorders the data so that the 2nd turbine is always infront of 3rd
                                wind_path_array = self.helper.sort_array_ascendX(wind_path_array)

                                ax_3t.scatter(wind_path_array[0,0], wind_path_array[0,1], color = "brown", marker="o", alpha=0.2)
                                ax_3t1.scatter(wind_path_array[0,0], wind_path_array[0,1],color = "brown", marker="o", alpha=0.2)
                                ax_3t2.scatter(wind_path_array[0,0], wind_path_array[0,1], color = "brown", marker="o", alpha=0.2)

                                ax_3t.scatter(wind_path_array[1,0], wind_path_array[1,1], color = "burlywood", marker="o", alpha=0.35)
                                ax_3t1.scatter(wind_path_array[1,0], wind_path_array[1,1], color = "burlywood", marker="o", alpha=0.35)

                                ax_3t.scatter(wind_path_array[2,0], wind_path_array[2,1], color = "powderblue", marker="o", alpha=0.35)
                                ax_3t2.scatter(wind_path_array[2,0], wind_path_array[2,1], color = "powderblue", marker="o", alpha=0.35)

                                wind_path_array = np.array([[0., 0.], [0., 0.], [0.,0.]])

                            temp_x = float(row[0])
                            temp_y = float(row[1])
                            turb_val = float(row[5])

                            #Add turbine positions to temporary array
                            if turb_val == 0:
                                wind_path_array[0,0] = temp_x
                                wind_path_array[0,1] = temp_y
                                count+= 1

                            elif turb_val == 1:
                                wind_path_array[1,0] = temp_x
                                wind_path_array[1,1] = temp_y
                                count+= 1

                            elif turb_val == 2:
                                wind_path_array[2,0] = temp_x
                                wind_path_array[2,1] = temp_y
                                count+= 1
                                
                line_count += 1

        ax_3t.set(title="Three Turbine Data Distribution")
        ax_3t.legend(handles=legend_elements_3t, loc="upper right")

        ax_3t1.set(title="Three Turbine, 2nd Turbine Data Distribution")
        ax_3t1.legend(handles=legend_elements_3t, loc="upper right")

        ax_3t2.set(title="Three Turbine, 3rd Turbine Data Distribution")
        ax_3t2.legend(handles=legend_elements_3t, loc="upper right")

        plt.show()

    def display_3T_windpath(self):
        #Creates a figure and its component axis to which we can plot the data.
        fig_3t = plt.figure(figsize=(40, 12))
        ax_3t = fig_3t.add_subplot(111)

        with open(self.filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            line_count = 0

            count = 0

            wind_path_array = np.array([[0., 0.], [0., 0.], [0.,0.]])
            
        #In each row the loop checks if we are still in the 3 turbine area and then extracts the coordinates.
            for row in csv_reader:
                if line_count > 0:

                    num_turb = int(row[3])
                    if num_turb == 3:
                            #Every 3 turbines it plots a line between them.
                            if count % 3 == 0:
                                #Reorders the data so that the 2nd turbine is always infront of 3rd
                                wind_path_array = self.helper.sort_array_ascendX(wind_path_array)

                                #Plots the individual lines on the axis
                                ax_3t.plot(wind_path_array[:, 0], wind_path_array[:, 1],
                                        alpha = 0.2, linewidth = 1)

                                wind_path_array = np.array([[0., 0.], [0., 0.], [0.,0.]])

                            temp_x = float(row[0])
                            temp_y = float(row[1])
                            turb_val = float(row[5])

                            #Add turbine positions to temporary array
                            if turb_val == 0:
                                wind_path_array[0,0] = temp_x
                                wind_path_array[0,1] = temp_y
                                count+= 1

                            elif turb_val == 1:
                                wind_path_array[1,0] = temp_x
                                wind_path_array[1,1] = temp_y
                                count+= 1

                            elif turb_val == 2:
                                wind_path_array[2,0] = temp_x
                                wind_path_array[2,1] = temp_y
                                count+= 1
                                #print(wind_path_array)

                line_count += 1

        ax_3t.set(title="Three Turbine Path Data")

        plt.show()

    def display_3T_predictors(self):

        #THIS REQUIRES FINGERPRINTS
        tu = GP_utility.Turbine_Helper()

        #Creates a figure and its component axis to which we can plot the data.
        fig_3t = plt.figure()

        ax_3t = Axes3D(fig_3t)

        #Fancy looking legend, I dont know how to do it simpler, if you wanna edit, be my guest.
        legend_elements_3t = [Line2D([0], [0], marker='o', color='w', label = "Turbine 0",
                                markerfacecolor='brown'),
                            Line2D([0], [0], marker='o', color='w', label = "Turbine 1",
                                markerfacecolor='burlywood'),
                            Line2D([0], [0], marker='o', color='w', label = "Turbine 2",
                                markerfacecolor='powderblue'),
                                ]

        with open(self.filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            line_count = 0

            count = 0

            wind_path_array = np.array([[0., 0.], [0., 0.], [0.,0.]])

        #In each row the loop checks if we are still in the 3 turbine area and then extracts the coordinates.
            for row in csv_reader:
                if line_count > 0:
                    num_turb = int(row[3])
                    if num_turb == 3:
                            if count % 3 == 0:
                                #Reorders the data so that the 2nd turbine is always infront of 3rd
                                wind_path_array = self.helper.sort_array_ascendX(wind_path_array)

                                #FINGERPRINTS TAKE THE POSITIONS AND NUMBER OF TURBINES AS ARGUMENTS RN ITS 3
                                fp = tu.fingerprint(wind_path_array,3)

                                ax_3t.scatter(fp[0,0], fp[0,1], fp[0,2], color = "brown", marker="o", alpha=0.2)

                                ax_3t.scatter(fp[1,0], fp[1,1], fp[1,2], color = "burlywood", marker="o", alpha=0.35)

                                ax_3t.scatter(fp[2,0], fp[2,1], fp[2,2], color = "powderblue", marker="o", alpha=0.35)
                                
                                wind_path_array = np.array([[0., 0.], [0., 0.], [0.,0.]])

                            #All this is the same as before with creating a temp array for each simulation.
                            temp_x = float(row[0])
                            temp_y = float(row[1])
                            turb_val = float(row[5])
                    
                            #Add turbine positions to temporary array
                            if turb_val == 0:
                                wind_path_array[0,0] = temp_x
                                wind_path_array[0,1] = temp_y
                                count+= 1

                            elif turb_val == 1:
                                wind_path_array[1,0] = temp_x
                                wind_path_array[1,1] = temp_y
                                count+= 1

                            elif turb_val == 2:
                                wind_path_array[2,0] = temp_x
                                wind_path_array[2,1] = temp_y
                                count+= 1
                                
                line_count += 1

        ax_3t.set(title="Three Turbine Data - Discriptor Distribution")
        ax_3t.legend(handles=legend_elements_3t, loc="upper right")

        plt.show()