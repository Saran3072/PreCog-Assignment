import json
import pandas as pd
import matplotlib.pyplot as plt

def plot_community_data(json_path):
    # Load data from JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Convert data to pandas DataFrame
    dates = []
    louvain_totals = []
    louvain_largest_ids = []
    louvain_largest_sizes = []
    girvan_totals = []
    girvan_largest_ids = []
    girvan_largest_sizes = []
    
    for date, info in data.items():
        dates.append(date)
        louvain_totals.append(info['louvain']['total_communities'])
        louvain_largest_ids.append(info['louvain']['largest_community'])
        louvain_largest_sizes.append(info['louvain']['size_of_largest_community'])
        girvan_totals.append(info['girvan']['total_communities'])
        girvan_largest_ids.append(info['girvan']['largest_community'])
        girvan_largest_sizes.append(info['girvan']['size_of_largest_community'])

    df = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'louvain_Total_Communities': louvain_totals,
        'louvain_Largest_Community_ID': louvain_largest_ids,
        'louvain_Size_of_Largest_Community': louvain_largest_sizes,
        'Girvan_Total_Communities': girvan_totals,
        'Girvan_Largest_Community_ID': girvan_largest_ids,
        'Girvan_Size_of_Largest_Community': girvan_largest_sizes
    })
    df.set_index('Date', inplace=True)

    # Plotting
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12), sharex=True)
    
    # louvain plot
    df['louvain_Total_Communities'].plot(ax=axes[0], marker='o', color='b', label='Total Communities', linestyle='-')
    axes[0].scatter(df.index, df['louvain_Largest_Community_ID'], color='r', label='Largest Community ID')
    axes[0].scatter(df.index, df['louvain_Size_of_Largest_Community'], color='g', label='Size of Largest Community')
    for i, txt in enumerate(df['louvain_Largest_Community_ID']):
        axes[0].annotate(txt, (df.index[i], df['louvain_Largest_Community_ID'][i]))
    for i, txt in enumerate(df['louvain_Size_of_Largest_Community']):
        axes[0].annotate(txt, (df.index[i], df['louvain_Size_of_Largest_Community'][i]))
    axes[0].set_title('louvain Community Detection Over Time')
    axes[0].set_ylabel('Values')
    axes[0].grid(True)
    axes[0].legend()

    # Girvan plot
    df['Girvan_Total_Communities'].plot(ax=axes[1], marker='o', color='b', label='Total Communities', linestyle='-')
    axes[1].scatter(df.index, df['Girvan_Largest_Community_ID'], color='r', label='Largest Community ID')
    axes[1].scatter(df.index, df['Girvan_Size_of_Largest_Community'], color='g', label='Size of Largest Community')
    for i, txt in enumerate(df['Girvan_Largest_Community_ID']):
        axes[1].annotate(txt, (df.index[i], df['Girvan_Largest_Community_ID'][i]))
    for i, txt in enumerate(df['Girvan_Size_of_Largest_Community']):
        axes[1].annotate(txt, (df.index[i], df['Girvan_Size_of_Largest_Community'][i]))
    axes[1].set_title('Girvan Community Detection Over Time')
    axes[1].set_ylabel('Values')
    axes[1].set_xlabel('Date')
    axes[1].grid(True)
    axes[1].legend()

    plt.savefig("analysis.png")
    plt.close()

# Example usage
plot_community_data('analysis.json')