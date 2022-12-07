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

def max_map(a,b):
    if a > 0.0:
        return 1.0
    return 0.0

def load_med_data(batch_size = 1):
    data_dim = 512

    dataset_training = datasets.ImageFolder('./data/training/training', transform=transforms.Compose([transforms.Resize((data_dim,data_dim)),transforms.ToTensor()]))
    dataset_target = datasets.ImageFolder('./data/training/target', transform=transforms.Compose([transforms.Resize((data_dim,data_dim)) , transforms.ToTensor()]))
    class ImageMapDataset(torch.utils.data.Dataset):
        def __init__(self, input_data, target_data):
        
            self.tensor_data = []     
            self.tensor_target = []
            for i in range(0,len(input_data)):
                self.tensor_data.append(input_data[i][0])
                tar = target_data[i][0]
                tar[tar > 0.0] = 1
                self.tensor_target.append(tar)
        
        # Stack lists into tensors and ship to GPU
            self.tensor_data = torch.stack(self.tensor_data).to(device)
            self.tensor_target = torch.stack(self.tensor_target).to(device)
        
        
        
        def __len__(self):
            return self.tensor_data.shape[0]
        def __getitem__(self, idx):
            return self.tensor_data[idx], self.tensor_target[idx]
    data =  ImageMapDataset(dataset_training, dataset_target)
    # finally a dataloader I can be happy with!!
    return (torch.utils.data.DataLoader(dataset=data, batch_size=batch_size, shuffle=True, num_workers=0) , data)

