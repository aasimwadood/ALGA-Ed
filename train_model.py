
import argparse
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from models import ALGAEdModel
from preprocess import preprocess_dataset
from model_selection import train_test_split
import pandas as pd
import os

def train_model(config):
    # Load and preprocess dataset
    data = preprocess_dataset(config['dataset_path'], config['disability_type'])
    features = data.drop('label', axis=1).values
    labels = data['label'].values

    # Split data
    X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Convert to tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.long)
    X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
    y_val_tensor = torch.tensor(y_val, dtype=torch.long)

    # Data loaders
    train_loader = DataLoader(list(zip(X_train_tensor, y_train_tensor)), batch_size=config['batch_size'], shuffle=True)
    val_loader = DataLoader(list(zip(X_val_tensor, y_val_tensor)), batch_size=config['batch_size'])

    # Initialize model
    model = ALGAEdModel(input_dim=X_train.shape[1], num_classes=config['num_classes'])
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=config['learning_rate'])

    # Training loop
    for epoch in range(config['epochs']):
        model.train()
        total_loss = 0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch+1}/{config['epochs']}, Loss: {total_loss/len(train_loader):.4f}")

        # Validation loop
        model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for inputs, targets in val_loader:
                outputs = model(inputs)
                _, predicted = torch.max(outputs, 1)
                total += targets.size(0)
                correct += (predicted == targets).sum().item()
        print(f"Validation Accuracy: {100 * correct / total:.2f}%")

    # Save model
    os.makedirs(config['save_path'], exist_ok=True)
    torch.save(model.state_dict(), os.path.join(config['save_path'], 'algaed_model.pt'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True)
    args = parser.parse_args()

    import yaml
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    train_model(config)
