import numpy as np
j = 0
turb_array = np.array([[3, 2, 5, 6, 8, 11], [1, 4, 4, 4, 4, 4]])
_ = np.array(turb_array[j,:])
__ = np.array(turb_array[j + 1,:])
print(_)
print(__)
turb_array[j,:] = __
turb_array[j+1, :] = _
print(turb_array)