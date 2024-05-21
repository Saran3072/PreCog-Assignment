import matplotlib.pyplot as plt
import networkx as nx

class CommunityVisualizer:
    @staticmethod
    def visualize_communities(graph, communities, path, title="Community Structure"):
        """
        Visualizes the graph with nodes colored by their community and nodes in the same community clustered together.

        Args:
            communities (dict): A dictionary mapping node identifiers to their community.
            title (str): The title of the plot.
        """
        # Create a color map from communities
        color_map = [communities[node] for node in graph.nodes()]

        # Initial position using spring layout
        pos = nx.spring_layout(graph, seed=42)  # Use a fixed seed for reproducibility

        # Adjust positions to bring same community nodes closer
        community_positions = {}
        for node, community in communities.items():
            if community not in community_positions:
                community_positions[community] = pos[node]
            else:
                # Adjust position slightly towards the community's mean position
                community_positions[community] = (community_positions[community][0] + pos[node][0]) / 2, \
                                                 (community_positions[community][1] + pos[node][1]) / 2

        final_pos = {}
        for node, community in communities.items():
            base_pos = community_positions[community]
            node_pos = pos[node]
            # Adjust node position towards the community's average position
            final_pos[node] = (base_pos[0] + node_pos[0]) / 2, (base_pos[1] + node_pos[1]) / 2

        plt.figure(figsize=(30, 30))
        # Draw the graph
        nx.draw(graph, final_pos, node_color=color_map, with_labels=True, cmap=plt.cm.Set3, node_size=100, font_size=8)
        plt.title(title)
        plt.savefig(path)
        plt.close()