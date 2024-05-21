import networkx as nx
from community import community_louvain
from networkx.algorithms.community import girvan_newman
# import infomap

class CommunityDetector:
    def __init__(self, ):
        """
        Initializes the CommunityDetector with a directed graph.
        """

    def detect_communities_louvain(self, graph):
        """
        Detects communities in a directed graph using the Louvain method adapted for directed graphs.

        Returns:
            dict: A dictionary mapping node identifiers to their respective community.
        """
        # Convert the directed graph to an undirected graph for Louvain method
        undirected_graph = graph.to_undirected()
        partition = community_louvain.best_partition(undirected_graph)
        return partition

    def detect_communities_girvan_newman(self, graph, num_communities=2):
        """
        Detects communities in a directed graph using the Girvan-Newman algorithm.

        Args:
            num_communities (int): The number of communities to detect.

        Returns:
            list: A list of sets, where each set contains the nodes that make up a community.
        """
        # Convert the directed graph to an undirected graph for Girvan-Newman method
        undirected_graph = graph.to_undirected()
        communities_generator = girvan_newman(undirected_graph)
        limited_communities = []
        for communities in communities_generator:
            limited_communities.append(communities)
            if len(communities) >= num_communities:
                break
        community_dict = {}
        for idx, community in enumerate(list(limited_communities[-1])):
            for node in community:
                community_dict[node] = idx
        return community_dict
