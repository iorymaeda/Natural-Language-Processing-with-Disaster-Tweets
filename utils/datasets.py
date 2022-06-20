import random

import numpy as np
import torch
from torch.utils.data import Dataset


class EmbeddingDataset(Dataset):
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y

    def shape(self):
        return self.x.shape
    
    def __len__(self):
        return len(self.y)
    
    def __getitem__(self, idx):
        x = self.x[idx]
        y = self.y[idx]
        return x, y



class NLPDataset(Dataset):
    def __init__(self, x, y, rand=False, **kwargs):
        """`rand` will balance classes"""
        self.x = x
        self.y = torch.LongTensor(y)      
        
        self.rand = rand
        if rand:
            self.classes = list(set(y))
            self.indeces = np.arange(0, len(y))
    
    def __len__(self):
        return len(self.y)
    
    
    def __getitem__(self, idx):
        if self.rand:
            target_class = random.choice(self.classes)
            idx = self.indeces[self.y == target_class]
            idx = random.choice(idx)
            
        x = {k: v[idx] for k, v in self.x.items()}
        y = self.y[idx]
        return y, x['input_ids'], x['attention_mask'], x['token_type_ids']


