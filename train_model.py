import argparse
import yaml
import torch
import torch.nn as nn
import torch.optim as optim
from utils import preprocess
from models import EngagementPredictor

def main(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    X, y = preprocess.load_data(config["data_path"])
    X = preprocess.preprocess(X)
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32).unsqueeze(1)

    model = EngagementPredictor(input_dim=X.shape[1])
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        optimizer.zero_grad()
        outputs = model(X_tensor)
        loss = criterion(outputs, y_tensor)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

    torch.save(model.state_dict(), config["model_save_path"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)
