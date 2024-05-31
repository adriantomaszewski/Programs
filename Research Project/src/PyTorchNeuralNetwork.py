import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset, random_split
import torch.nn as nn
import torch.nn.functional as F

# # of times to run and save the model
MODEL_TRAIN_COUNT = 25

# Hyperparameters
input_size = 34
hidden_size = 100
output_size = 1
num_epochs = 100
learning_rate = 0.01

# Load data
data = pd.read_csv('/Users/adrian/Downloads/dermatology/dermatology.data')
data.columns = ['erythema', 'scaling', 'definite_borders', 'itching', 'koebner_phenomenon', 'polygonal_papules', 
                'follicular_papules', 'oral_mucosal_involvement', 'knee_and_elbow_involvement', 'scalp_involvement', 
                'family_history', 'melanin_incontinence', 'eosinophils_in_the_infiltrate', 'PNL_infiltrate', 
                'fibrosis_of_the_papillary_dermis', 'exocytosis', 'acanthosis', 'hyperkeratosis', 'parakeratosis', 
                'clubbing_of_the_rete_ridges', 'elongation_of_the_rete_ridges', 'thinning_of_the_suprapapillary_epidermis', 
                'spongiform_pustule', 'munro_microabcess', 'focal_hypergranulosis', 'disappearance_of_the_granular_layer', 
                'vacuolisation_and_damage_of_basal_layer', 'spongiosis', 'saw-tooth_appearance_of_retes', 
                'follicular_horn_plug', 'perifollicular_parakeratosis', 'inflammatory_monoluclear_inflitrate', 
                'band-like_infiltrate', 'age', 'class']
data.replace('?', pd.NA, inplace=True)
data.dropna(inplace=True)

# Convert 'age' to numeric
data['age'] = pd.to_numeric(data['age'])

# Seting the last column as the target and the rest as features
features = data.iloc[:, :-1].values
targets = data.iloc[:, -1].values

# Convert to PyTorch tensors
features_tensor = torch.tensor(features, dtype=torch.float32)
targets_tensor = torch.tensor(targets, dtype=torch.float32)

# Create a dataset and split into training and validation sets
dataset = TensorDataset(features_tensor, targets_tensor)
train_size = int(0.7 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Define neural network
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        x = self.fc3(x) 
        return x 
for model_train_count in range(0, MODEL_TRAIN_COUNT):
    model = SimpleNN(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


    # Lists to store accuracy and loss for each epoch
    train_losses = []
    val_losses = []
    train_accuracies = []
    val_accuracies = []
    val_loss = 0
    val_correct = 0
    val_total = 0

    for epoch in range(num_epochs):
        model.train()
        train_correct = 0
        train_total = 0.0001
        running_loss = 0.0
        
        for batch_features, batch_labels in train_loader:
            # Zero the parameter gradients
            optimizer.zero_grad()
            
            # Forward pass
            outputs = model(batch_features)
            loss = criterion(outputs.squeeze(), batch_labels)
            
            # Backward pass and optimization
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        
        epoch_loss = running_loss / len(train_loader)
        # Print epoch loss
        if (epoch+1) % 5 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    model.eval()

    with torch.no_grad():
        for batch_features, batch_labels in val_loader:
            outputs = model(batch_features)
            loss = criterion(outputs.squeeze(), batch_labels)
            val_loss += loss.item()
            
            # Calculate validation accuracy
            predicted = torch.round(outputs.squeeze())  # Round predictions to the nearest integer
            val_total += batch_labels.size(0)
            val_correct += (predicted == batch_labels).sum().item()
        
        val_loss /= len(val_loader)
        val_accuracy = 100 * val_correct / val_total
        val_losses.append(val_loss)
        val_accuracies.append(val_accuracy)
        print(f'Validation Loss: {val_loss:.4f}, Validation Accuracy: {val_accuracy:.2f}%')
        
    # Save the results to a text document
    results_file = '/Users/adrian/Documents/Research Project/NeuralNetworkLossandAccuracyData.csv'
    with open(results_file, 'a') as f:
        f.write(f'{val_losses[0]:.4f},{val_accuracies[0]:.2f}\n')
    print(f'Results saved to {results_file}')

    # Save the model
    model_save_path = '/Users/adrian/Documents/Programs/Research Project/models.pth'
    torch.save(model.state_dict(), model_save_path)
    print(f'Model saved to {model_save_path}')

    f.close()