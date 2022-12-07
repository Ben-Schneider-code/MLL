#!/usr/bin/env python
# coding: utf-8

# # Using CNN Model for Medical Image Segmentation
# ![CNN.JPG](attachment:CNN.JPG)

# In[1]:


import torch
import torchvision
from torchvision import transforms, datasets
import numpy as np
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.nn.functional as F 

if torch.cuda.is_available():  
    dev = "cuda:0"
else:
    dev = "cpu"
device = torch.device(dev)
print(device)


# In[2]:


transform = transforms.Compose([transforms.ToTensor()])
dataset = datasets.ImageFolder('./data/training/', transform=transform)

