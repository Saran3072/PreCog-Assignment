import networkx as nx
from datetime import datetime, timedelta

class DataLoader:
    @staticmethod
    def load_graph(edges_file, dates_file):
        """
        Loads the graph from edges and dates files.

        Args:
            edges_file (str): Path to the file containing the graph edges.
            dates_file (str): Path to the file containing the publication dates.

        Returns:
            nx.DiGraph: The directed graph with nodes annotated with publication dates.
            dict: Dictionary with node IDs as keys and datetime objects as values.
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
                dates[paper_id] = datetime.strptime(date, "%Y-%m-%d")

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

        return graph, dates

    @staticmethod
    def create_incremental_graphs(graph, dates, num_months=36):
        """
        Creates incremental graphs for each month up to num_months.

        Args:
            graph (nx.DiGraph): The original directed graph.
            dates (dict): Dictionary of node dates.
            num_months (int): Number of months to create incremental graphs.

        Returns:
            dict: Dictionary with keys as dates and values as networkx graphs.
        """
        min_date = min(dates.values())
        graphs_dict = {}

        for month in range(num_months):
            end_date = min_date + timedelta(days=30*month)
            subgraph = nx.DiGraph()

            for node, date in dates.items():
                if date <= end_date:
                    if node not in subgraph:
                        subgraph.add_node(node, date=date)

            for from_node, to_node in graph.edges:
                if from_node in subgraph and to_node in subgraph:
                    subgraph.add_edge(from_node, to_node)

            graphs_dict[end_date.strftime("%Y-%m")] = subgraph

        return graphs_dict