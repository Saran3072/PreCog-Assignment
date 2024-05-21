from node2vec import Node2Vec

def generate_node2vec_embeddings(graph):
    """
    Generates Node2Vec embeddings for the graph.
    
    Args:
        graph (nx.DiGraph): The directed graph.

    Returns:
        dict: Node embeddings.
    """
    node2vec = Node2Vec(graph, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    embeddings = {str(node): model.wv[str(node)] for node in graph.nodes()}
    
    return embeddings
