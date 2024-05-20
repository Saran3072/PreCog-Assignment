import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class CommunityDetector:
    @staticmethod
    def girvan_newman(graph, num_communities=2):
        # This generator will yield sets of communities at each iteration
        communities_generator = nx.community.girvan_newman(graph)
        # We'll take the communities after a certain number of iterations, let's say until we have num_communities
        for communities in communities_generator:
            if len(communities) >= num_communities:
                return communities
    