import os
import networkx as nx
import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def visualize_graph(incremental_graphs, date_key):
        """
        Visualize a graph for a particular date key.

        Args:
            incremental_graphs (dict): Dictionary where keys are date strings and values are corresponding graphs.
            date_key (str): The date key for which the graph needs to be visualized.
        """
        graph = incremental_graphs.get(date_key, None)
        if graph is None:
            print("No graph available for the specified date.")
            return

        plt.figure(figsize=(50, 50))
        pos = nx.spring_layout(graph)  # Positions for all nodes
        nx.draw(graph, pos, with_labels=True, node_size=300, node_color="skyblue", font_size=8)
        plt.title(f"Graph for {date_key}")
        plt.savefig(os.path.join('./graphs', f'{date_key}.png'))
        plt.close()