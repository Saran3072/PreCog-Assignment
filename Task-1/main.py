from data_loader import GraphLoader
from graph_analyzer import GraphAnalyzer
from plotter import Plotter

if __name__ == '__main__':
    graph_loader = GraphLoader('./data/Cit-HepPh.txt', './data/cit-HepPh-dates.txt')
    graph = graph_loader.load_graph()

    analyzer = GraphAnalyzer(graph)
    properties = analyzer.analyze_yearly_graphs()

    folder_path = './properties'  # Adjust the folder path if needed
    output_folder = './plots'     # Folder to save the plots
    properties, years = Plotter.load_properties(folder_path)
    Plotter.plot_properties(properties, years, output_folder)
