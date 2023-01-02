#converts mat file into csv

import pandas as pd
from scipy.io import loadmat
import numpy as np
import sys
import mat73

data_dict = loadmat(sys.argv[1])

# use this for MATLAB 7.3 files
# data_dict = mat73.loadmat(sys.argv[1])

arr = np.array( data_dict['X'] ) 
# arr = arr[:,0]
print(arr)
pd.DataFrame(arr).to_csv(sys.argv[2], header=None, index=None)