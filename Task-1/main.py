from data_loader import GraphLoader
from graph_analyzer import GraphAnalyzer
from plotter import Plotter

if __name__ == '__main__':
    graph_loader = GraphLoader('./data/Cit-HepPh.txt', './data/cit-HepPh-dates.txt')
    graph = graph_loader.load_graph()
    
    print(graph)

    analyzer = GraphAnalyzer(graph)
    properties = analyzer.analyze_yearly_graphs()

    # Plotter.plot_properties(properties)