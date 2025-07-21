import argparse
import torch
from utils import preprocess
from models import EngagementPredictor

def main(test_path, model_path):
    X, y = preprocess.load_data(test_path)
    X = preprocess.preprocess(X)
    X_tensor = torch.tensor(X, dtype=torch.float32)

    model = EngagementPredictor(input_dim=X.shape[1])
    model.load_state_dict(torch.load(model_path))
    model.eval()

    preds = model(X_tensor).detach().numpy()
    print("Sample Predictions:", preds[:5])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--model", default="model.pth")
    args = parser.parse_args()
    main(args.input, args.model)
