from graph_loader import load_graph, get_yearly_graphs
from node2vec_embeddings import generate_node2vec_embeddings
from classifier import train_classifier, evaluate_classifier, prepare_data

# Load the graph
edges_file = '/kaggle/input/graphnets/Cit-HepPh.txt'
dates_file = '/kaggle/input/graphnets/cit-HepPh-dates.txt'
graph = load_graph(edges_file, dates_file)
yearly_graphs = get_yearly_graphs(graph)
graph = yearly_graphs[1995]

# Generate Node2Vec embeddings
embeddings = generate_node2vec_embeddings(graph)

# Prepare data
X_train, y_train, X_test, y_test = prepare_data(graph)

# Train the classifier
clf = train_classifier(X_train, y_train, embeddings)

# Evaluate the classifier
auc_roc = evaluate_classifier(clf, X_test, y_test, embeddings)
print("AUC-ROC:", auc_roc)