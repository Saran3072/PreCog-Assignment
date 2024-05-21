import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import networkx as nx
import matplotlib.pyplot as plt

def get_edge_features(embeddings, edges):
    """
    Generates features for edges based on node embeddings.
    
    Args:
        embeddings (dict): Node embeddings.
        edges (list of tuples): List of edges (from_node, to_node).

    Returns:
        np.array: Edge features.
    """
    edge_features = []
    for from_node, to_node in edges:
        if from_node in embeddings and to_node in embeddings:
            edge_features.append(np.concatenate([embeddings[from_node], embeddings[to_node]]))
    return np.array(edge_features)

def prepare_data(graph, test_size=0.3):
    """
    Prepares training and testing data for link prediction.
    
    Args:
        graph (nx.DiGraph): The graph.
        test_size (float): The proportion of the dataset to include in the test split.

    Returns:
        tuple: Training and testing edges and labels.
    """
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

def train_classifier(X_train, y_train, embeddings):
    """
    Trains a logistic regression classifier for link prediction.
    
    Args:
        X_train (list of tuples): Training edges.
        y_train (np.array): Training labels.
        embeddings (dict): Node embeddings.

    Returns:
        LogisticRegression: Trained classifier.
    """
    train_features = get_edge_features(embeddings, X_train)

    clf = LogisticRegression()
    clf.fit(train_features, y_train)
    
    return clf

def evaluate_classifier(clf, X_test, y_test, embeddings):
    """
    Evaluates the classifier on the test set and plots the ROC curve.
    
    Args:
        clf (LogisticRegression): Trained classifier.
        X_test (list of tuples): Test edges.
        y_test (np.array): Test labels.
        embeddings (dict): Node embeddings.

    Returns:
        float: AUC-ROC score.
    """
    test_features = get_edge_features(embeddings, X_test)
    test_predictions = clf.predict_proba(test_features)[:, 1]
    
    auc_roc = roc_auc_score(y_test, test_predictions)
    
    return auc_roc
