import networkx as nx

class GraphLoader:
    def __init__(self, edges_file, dates_file):
        """
        Initializes the GraphLoader with file paths for edges and dates.

        Args:
            edges_file (str): Path to the file containing the graph edges.
            dates_file (str): Path to the file containing the publication dates.
        """
        self.edges_file = edges_file
        self.dates_file = dates_file
        self.graph = nx.DiGraph()

    def load_graph(self):
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
        with open(self.dates_file, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                parts = line.strip().split()
                paper_id = parts[0]
                date = parts[1]
                dates[paper_id] = date

        # Load the graph
        with open(self.edges_file, 'r') as file:
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
