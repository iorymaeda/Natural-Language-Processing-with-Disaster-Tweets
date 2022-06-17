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