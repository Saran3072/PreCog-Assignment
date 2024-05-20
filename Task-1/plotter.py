import os
import json
import matplotlib.pyplot as plt

class Plotter:
    @staticmethod
    def load_properties(folder_path):
        properties = {
            "density": [],
            "average_clustering": [],
            "connected_components": [],
            "degree_centrality": [],
            "betweenness_centrality": [],
            "closeness_centrality": [],
            "pagerank": []
        }
        years = []

        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith('.json'):
                year = filename.split('.')[0]
                years.append(year)
                with open(os.path.join(folder_path, filename), 'r') as file:
                    data = json.load(file)
                    properties["density"].append(data["density"])
                    properties["average_clustering"].append(data["average_clustering"])
                    properties["connected_components"].append(data["connected_components"])
                    properties["degree_centrality"].append(data["degree_centrality"])
                    properties["betweenness_centrality"].append(data["betweenness_centrality"])
                    properties["closeness_centrality"].append(data["closeness_centrality"])
                    properties["pagerank"].append(data["pagerank"])
        
        return properties, years

    @staticmethod
    def plot_properties(properties, years, output_folder):
        os.makedirs(output_folder, exist_ok=True)
        
        plt.figure(figsize=(15, 10))
        
        plt.subplot(2, 4, 1)
        plt.plot(years, properties["density"], marker='o')
        plt.title('Density')
        plt.xlabel('Year')
        plt.ylabel('Density')
        plt.savefig(os.path.join(output_folder, 'density.png'))

        plt.subplot(2, 4, 2)
        plt.plot(years, properties["average_clustering"], marker='o')
        plt.title('Average Clustering')
        plt.xlabel('Year')
        plt.ylabel('Average Clustering')
        plt.savefig(os.path.join(output_folder, 'average_clustering.png'))

        plt.subplot(2, 4, 3)
        plt.plot(years, properties["connected_components"], marker='o')
        plt.title('Connected Components')
        plt.xlabel('Year')
        plt.ylabel('Connected Components')
        plt.savefig(os.path.join(output_folder, 'connected_components.png'))

        plt.subplot(2, 4, 4)
        plt.plot(years, properties["degree_centrality"], marker='o')
        plt.title('Degree Centrality')
        plt.xlabel('Year')
        plt.ylabel('Degree Centrality')
        plt.savefig(os.path.join(output_folder, 'degree_centrality.png'))

        plt.subplot(2, 4, 5)
        plt.plot(years, properties["betweenness_centrality"], marker='o')
        plt.title('Betweenness Centrality')
        plt.xlabel('Year')
        plt.ylabel('Betweenness Centrality')
        plt.savefig(os.path.join(output_folder, 'betweenness_centrality.png'))

        plt.subplot(2, 4, 6)
        plt.plot(years, properties["closeness_centrality"], marker='o')
        plt.title('Closeness Centrality')
        plt.xlabel('Year')
        plt.ylabel('Closeness Centrality')
        plt.savefig(os.path.join(output_folder, 'closeness_centrality.png'))

        plt.subplot(2, 4, 7)
        plt.plot(years, properties["pagerank"], marker='o')
        plt.title('PageRank')
        plt.xlabel('Year')
        plt.ylabel('PageRank')
        plt.savefig(os.path.join(output_folder, 'pagerank.png'))

        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, 'all_properties.png'))
        plt.close()

def main():
    folder_path = './properties'  # Adjust the folder path if needed
    output_folder = './plots'     # Folder to save the plots
    properties, years = load_properties(folder_path)
    plot_properties(properties, years, output_folder)

if __name__ == "__main__":
    main()
