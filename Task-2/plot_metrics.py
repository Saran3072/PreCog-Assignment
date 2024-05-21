import matplotlib.pyplot as plt
import json

def plot_community_detection_scores(json_file_path):
    """
    Reads a JSON file with community detection scores and plots them.

    Args:
    json_file_path (str): Path to the JSON file containing the scores.

    """
    # Read data from JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Extracting data for plotting
    dates = list(data.keys())
    louvian_scores = [data[date]['louvian'] for date in dates]
    girvan_scores = [data[date]['girvan'] for date in dates]

    # Plotting
    plt.figure(figsize=(20, 20))  # Set the figure size
    plt.plot(dates, louvian_scores, label='Louvian', color='blue', marker='o')  # Louvian line
    plt.plot(dates, girvan_scores, label='Girvan', color='green', marker='o')  # Girvan line

    plt.title('Community Detection Evaluation with Modularity Metric Over Time')  # Title of the plot
    plt.xlabel('Dates')  # Label for the x-axis
    plt.ylabel('Score')  # Label for the y-axis
    plt.xticks(rotation=45)  # Rotate dates for better readability
    plt.legend()  # Add a legend to distinguish the lines

    plt.tight_layout()  # Adjust layout to not cut off labels
    plt.savefig("results.png")
    plt.close()