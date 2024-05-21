import networkx as nx
from datetime import datetime
from sklearn.model_selection import train_test_split
import numpy as np
import torch
from torch_geometric.data import Data

import networkx as nx

def load_graph(edges_file, dates_file):
    """
    Loads the graph from edges and dates files.

    Args:
        edges_file (str): Path to the file containing the graph edges.
        dates_file (str): Path to the file containing the publication dates.

    Returns:
        nx.DiGraph: The directed graph with nodes annotated with publication dates.
    """
    graph = nx.DiGraph()
    dates = {}

    # Load dates from the dates file
    with open(dates_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split()
            paper_id = parts[0]
            date = parts[1]
            dates[paper_id] = date

    # Load the graph
    with open(edges_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            from_node, to_node = line.strip().split()
            if from_node in dates and to_node in dates:  # Ensure both nodes have dates
                if from_node not in graph:
                    graph.add_node(from_node, date=dates[from_node])
                if to_node not in graph:
                    graph.add_node(to_node, date=dates[to_node])
                graph.add_edge(from_node, to_node)

    return graph

def get_yearly_graphs(graph):
    """
    Generate yearly cumulative graphs based on publication dates stored in node attributes.
    """
    # Extract years from node date attributes
    years = [int(graph.nodes[node]['date'].split('-')[0]) for node in graph]
    start_year, end_year = min(years), max(years)

    yearly_graphs = {}
    for year in range(start_year, end_year + 1):
        filtered_graph = nx.DiGraph()
        for node in graph:
            node_date = int(graph.nodes[node]['date'].split('-')[0])
            if node_date <= year:
                for to_node in graph.successors(node):
                    to_node_date = int(graph.nodes[to_node]['date'].split('-')[0])
                    if to_node_date <= year:
                        filtered_graph.add_edge(node, to_node)

        yearly_graphs[year] = filtered_graph

    return yearly_graphs

def prepare_data(graph, test_size=0.3):
    edges = list(graph.edges)
    non_edges = list(nx.non_edges(graph))
    non_edges = non_edges[:len(edges)]  # Balance positive and negative samples

    X_edges, X_edges_test = train_test_split(edges, test_size=test_size, random_state=42)
    X_non_edges, X_non_edges_test = train_test_split(non_edges, test_size=test_size, random_state=42)

    X_train = X_edges + X_non_edges
    y_train = np.concatenate([np.ones(len(X_edges)), np.zeros(len(X_non_edges))])

    X_test = X_edges_test + X_non_edges_test
    y_test = np.concatenate([np.ones(len(X_edges_test)), np.zeros(len(X_non_edges_test))])

    return X_train, y_train, X_test, y_test

def create_data_object(graph, X_train, y_train, node_mapping):
    x = torch.eye(len(node_mapping))  # Use identity matrix as node features (one-hot encoding)
    edge_index = torch.tensor([[node_mapping[u], node_mapping[v]] for u, v in X_train], dtype=torch.long).t().contiguous()
    y = torch.tensor(y_train, dtype=torch.float)
    data = Data(x=x, edge_index=edge_index, y=y)
    data.train_mask = data.val_mask = data.test_mask = None
    return data
