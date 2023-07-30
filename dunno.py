import numpy as np
j = 0
turb_array = np.array([[3, 2, 5, 6, 8, 11], [1, 4, 4, 4, 4, 4]])
turb_array[j, 5], turb_array[j + 1, 5] = turb_array[j + 1, 5], turb_array[j, 5]
print(turb_array)