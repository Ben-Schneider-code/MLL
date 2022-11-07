import pandas as pd
from scipy.io import loadmat
import numpy as np

data_dict = loadmat('http.mat')

arr = np.array( data_dict['X'] ) 
# arr = arr[:,0]
print(arr)
pd.DataFrame(arr).to_csv("http.csv", header=None, index=None)