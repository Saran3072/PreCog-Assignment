import networkx as nx
from sklearn.metrics import silhouette_score
import numpy as np

class CommunityEvaluator:
    @staticmethod
    def evaluate_modularity(graph, communities):
        """
        Evaluates the modularity of the given community structure.

        Args:
            communities (dict): A dictionary mapping node identifiers to their community.

        Returns:
            float: The modularity score.
        """
        # Convert community dictionary to partition list
        partition = [[] for _ in range(max(communities.values()) + 1)]
        for node, comm in communities.items():
            partition[comm].append(node)
        return nx.community.modularity(graph, partition)
    
    @staticmethod
    def evaluate_coverage(graph, communities):
        """
        Manually calculates the coverage of the given community structure.

        Args:
            communities (dict): A dictionary mapping node identifiers to their community.

        Returns:
            float: The coverage score.
        """
        partition = [[] for _ in range(max(communities.values()) + 1)]
        for node, comm in communities.items():
            partition[comm].append(node)

        intra_community_edges = 0
        total_edges = graph.number_of_edges()

        for community in partition:
            subgraph = graph.subgraph(community)
            intra_community_edges += subgraph.number_of_edges()

        coverage_score = intra_community_edges / total_edges if total_edges > 0 else 0
        return coverage_score

    @staticmethod
    def evaluate_silhouette(graph, communities):
        """
        Evaluates the community structure using the silhouette score.

        Args:
            communities (dict): A dictionary mapping node identifiers to their community.

        Returns:
            float: The silhouette score.
        """
        if len(set(communities.values())) < 2:
            return -1  # Silhouette score is not well-defined for a single cluster.

        # Create a feature matrix and label vector
        features = np.array([graph.nodes[n]['vector'] for n in graph.nodes()])  # Assuming nodes have feature vectors
        labels = np.array([communities[node] for node in graph.nodes()])
        return silhouette_score(features, labels)
