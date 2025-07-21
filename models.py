import torch
import torch.nn as nn

class EngagementPredictor(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=64, output_dim=1):
        super(EngagementPredictor, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)