from data_loader import DataLoader
from community_detection import CommunityDetector

edges_file = './data/Cit-HepPh.txt'
dates_file = './data/cit-HepPh-dates.txt'

graph, dates = DataLoader.load_graph(edges_file, dates_file)
incremental_graphs = DataLoader.create_incremental_graphs(graph, dates, num_months=12)