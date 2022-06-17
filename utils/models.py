import torch
from torch import nn


class ClassifierModel(nn.Module):
    def __init__(self, input_dim=32, output_dim=2, 
        d=[64, 64], callable_=None, dropout_p=0.5, **kwargs):
        super().__init__()
        
        seq = []
        d = [input_dim] + d + [output_dim]
        for i in range(len(d)-1):
            seq.append(
                nn.Linear(d[i], d[i+1])
            )
            seq.append(nn.Dropout(p=dropout_p))
            if i != len(d)-2:
                seq.append(nn.GELU())
                
        self.callable_ = callable_
        self.seq = nn.Sequential(*seq)

        
    def forward(self, x: torch.Tensor):
        if self.callable_ is not None:
            device = x.device
            x = torch.from_numpy(self.callable_(x.cpu()).astype('float32'))
            x = x.to(device)
            
        return self.seq(x)