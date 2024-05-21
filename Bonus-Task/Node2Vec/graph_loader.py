import networkx as nx

def load_graph(edges_file, dates_file):
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
    with open(dates_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split()
            paper_id = parts[0]
            date = parts[1]
            dates[paper_id] = date

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

    return graph

def get_yearly_graphs(graph):
    """
    Generate yearly cumulative graphs based on publication dates stored in node attributes.
    """
    # Extract years from node date attributes
    years = [int(graph.nodes[node]['date'].split('-')[0]) for node in graph]
    start_year, end_year = min(years), max(years)

    yearly_graphs = {}
    for year in range(start_year, end_year + 1):
        filtered_graph = nx.DiGraph()
        for node in graph:
            node_date = int(graph.nodes[node]['date'].split('-')[0])
            if node_date <= year:
                for to_node in graph.successors(node):
                    to_node_date = int(graph.nodes[to_node]['date'].split('-')[0])
                    if to_node_date <= year:
                        filtered_graph.add_edge(node, to_node)

        yearly_graphs[year] = filtered_graph

    return yearly_graphs