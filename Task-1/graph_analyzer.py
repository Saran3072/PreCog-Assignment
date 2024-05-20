import networkx as nx
import json

class GraphAnalyzer:
    """
    Performs various analyses on a set of cumulative year-wise graphs.
    """

    def __init__(self, graph):
        """
        Initialize the GraphAnalyzer with a graph.

        Args:
            graph (nx.DiGraph): The graph to analyze.
        """
        self.graph = graph
        self.yearly_graphs = self.get_yearly_graphs()

    def get_yearly_graphs(self):
        """
        Generate yearly cumulative graphs based on publication dates stored in node attributes.
        """
        # Extract years from node date attributes
        years = [int(self.graph.nodes[node]['date'].split('-')[0]) for node in self.graph]
        start_year, end_year = min(years), max(years)

        yearly_graphs = {}
        for year in range(start_year, end_year + 1):
            filtered_graph = nx.DiGraph()
            for node in self.graph:
                node_date = int(self.graph.nodes[node]['date'].split('-')[0])
                if node_date <= year:
                    for to_node in self.graph.successors(node):
                        to_node_date = int(self.graph.nodes[to_node]['date'].split('-')[0])
                        if to_node_date <= year:
                            filtered_graph.add_edge(node, to_node)

            yearly_graphs[year] = filtered_graph

        return yearly_graphs

    def analyze_yearly_graphs(self):
        """
        Analyzes the graphs for each year, computing various network properties,
        and saves the results as individual JSON files for each year.
        """
        for year, graph in self.yearly_graphs.items():
            properties = {
                'density': nx.density(graph),
                'average_clustering': nx.average_clustering(graph),
                'connected_components': nx.number_weakly_connected_components(graph),
                'degree_centrality': self.average_metric(nx.degree_centrality, graph),
                'betweenness_centrality': self.average_metric(nx.betweenness_centrality, graph),
                'closeness_centrality': self.average_metric(nx.closeness_centrality, graph),
                'pagerank': self.average_metric(nx.pagerank, graph)
            }

            # Save each year's properties to a separate JSON file
            file_name = f'./properties/{year}.json'
            with open(file_name, 'w') as file:
                json.dump(properties, file, indent=4)

    @staticmethod
    def average_metric(metric_func, graph):
        """
        Calculates the average value of a given centrality metric for the graph.
        """
        metric_values = metric_func(graph)
        if len(metric_values) > 0:
            return sum(metric_values.values()) / len(metric_values)
        return 0

