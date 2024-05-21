from datetime import datetime
import json
from data_loader import DataLoader
from community_detection import CommunityDetector 
from community_evaluation import CommunityEvaluator
from plot import CommunityVisualizer
from plot_metrics import *
from analysis import *
from plot_analytics import *

edges_file = './data/Cit-HepPh.txt'
dates_file = './data/cit-HepPh-dates.txt'

num_months = 24

graph, dates = DataLoader.load_graph(edges_file, dates_file)
incremental_graphs = DataLoader.create_incremental_graphs(graph, dates, num_months=num_months)

detector = CommunityDetector()

results = {}
analysis = {}

for date in incremental_graphs:
    metrics = {}
    start_date = datetime.strptime(date, '%Y-%m')
    if start_date > datetime.strptime('1992-05', '%Y-%m'):
        louvain_communities = detector.detect_communities_louvain(incremental_graphs[date])
        girvan_newman_communities = detector.detect_communities_girvan_newman(incremental_graphs[date])

        louvain_analysis = analyze_communities(louvain_communities)
        girvan_analysis = analyze_communities(girvan_newman_communities)
        
        analysis[date] = {
            "louvian": louvain_analysis,
            "girvan": girvan_analysis
            }
        
        CommunityVisualizer.visualize_communities(graph=incremental_graphs[date], communities=louvain_communities, path=f"./plots/louvian/{date}", title="Community Detectio with Louvian")
        CommunityVisualizer.visualize_communities(graph=incremental_graphs[date], communities=girvan_newman_communities, path=f"./plots/girvan/{date}", title="Community Detection with Girvan")

        metrics["louvian"] = CommunityEvaluator.evaluate_modularity(graph=incremental_graphs[date], communities=louvain_communities)
        metrics["girvan"] =  CommunityEvaluator.evaluate_modularity(graph=incremental_graphs[date], communities=girvan_newman_communities)
        
        results[date] = metrics

# Path where you want to save the JSON file
analytics_file_path = "analysis.json"
results_file_path = "results.json"

# Writing dictionary to JSON file
with open(analytics_file_path, 'w') as json_file:
    json.dump(analysis, json_file)

# Writing dictionary to JSON file
with open(results_file_path, 'w') as json_file:
    json.dump(results, json_file)

plot_community_data(analytics_file_path)
plot_community_detection_scores(results_file_path)