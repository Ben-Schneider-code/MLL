#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import pandas as pd

if len(sys.argv) < 4:
    print("not enough args")
    exit()
    


file_name = sys.argv[1]
dim = int(sys.argv[2])


# In[2]:



# In[3]:


col_names = []
for i in range(0,dim):
    col_names.append(str(i))
df = pd.read_csv(file_name, names=col_names, header=None)

target = col_names.pop()
df.rename(columns={target:'t'}, inplace=True)
col_names.append('t')
# Get one hot encoding of columns B
for column in col_names:
    one_hot = pd.get_dummies(df[column])
    
    new_names = []
    index = 0
    
    for key in one_hot.keys():
        new_names.append(column + "_"+ str(index))
        index = index+1
        
    one_hot.columns = new_names
    # Drop column B as it is now encoded
    df = df.drop(column,axis = 1)
    # Join the encoded df
    df = df.join(one_hot)


# In[4]:


df.to_csv(sys.argv[3], index=False)

