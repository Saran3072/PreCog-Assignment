from sklearn.metrics import roc_curve
import torch
import torch.optim as optim
from model import GraphSAGE
from data_loader import load_graph, prepare_data, create_data_object, get_yearly_graphs
from training import train, test

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the graph
graph = load_graph('./data/Cit-HepPh.txt', './data/cit-HepPh-dates.txt')
graphs = get_yearly_graphs(graph)
graph = graphs[1995]

# Prepare the data
X_train, y_train, X_test, y_test = prepare_data(graph)
node_mapping = {node: i for i, node in enumerate(graph.nodes())}
data = create_data_object(graph, X_train, y_train, node_mapping)

# Model setup
model = GraphSAGE(in_channels=data.x.size(1), hidden_channels=64, out_channels=32)
optimizer = optim.Adam(model.parameters(), lr=0.01)
model.to(device)

# Training loop
epochs = 20
for epoch in range(epochs):
    loss = train(model, optimizer, data, device)
    print(f'Epoch {epoch+1}, Loss: {loss}')

# Testing
results = test(model, data, X_test, y_test, node_mapping, device)
print(f'Test Results - AUC: {results[0]}, Precision: {results[1]}, Recall: {results[2]}, F1: {results[3]}')