import pandas as pd
import numpy as np
# From list
list_data = [10, 20, 30, 40]
s1 = pd.Series(list_data)
print("Series from list:\n", s1)
# From numpy array
array_data = np.array([5, 10, 15, 20])
s2 = pd.Series(array_data)
print("\nSeries from numpy array:\n", s2)
# From dictionary
dict_data = {'x': 1, 'y': 2, 'z': 3}
s3 = pd.Series(dict_data)
print("\nSeries from dictionary:\n", s3)
