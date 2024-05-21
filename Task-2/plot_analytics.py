import json
import pandas as pd
import matplotlib.pyplot as plt

def plot_community_data(json_path):
    # Load data from JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Convert data to pandas DataFrame
    dates = []
    louvian_totals = []
    louvian_largest_ids = []
    louvian_largest_sizes = []
    girvan_totals = []
    girvan_largest_ids = []
    girvan_largest_sizes = []
    
    for date, info in data.items():
        dates.append(date)
        louvian_totals.append(info['louvian']['total_communities'])
        louvian_largest_ids.append(info['louvian']['largest_community'])
        louvian_largest_sizes.append(info['louvian']['size_of_largest_community'])
        girvan_totals.append(info['girvan']['total_communities'])
        girvan_largest_ids.append(info['girvan']['largest_community'])
        girvan_largest_sizes.append(info['girvan']['size_of_largest_community'])

    df = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Louvian_Total_Communities': louvian_totals,
        'Louvian_Largest_Community_ID': louvian_largest_ids,
        'Louvian_Size_of_Largest_Community': louvian_largest_sizes,
        'Girvan_Total_Communities': girvan_totals,
        'Girvan_Largest_Community_ID': girvan_largest_ids,
        'Girvan_Size_of_Largest_Community': girvan_largest_sizes
    })
    df.set_index('Date', inplace=True)

    # Plotting
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12), sharex=True)
    
    # Louvian plot
    df['Louvian_Total_Communities'].plot(ax=axes[0], marker='o', color='b', label='Total Communities', linestyle='-')
    axes[0].scatter(df.index, df['Louvian_Largest_Community_ID'], color='r', label='Largest Community ID')
    axes[0].scatter(df.index, df['Louvian_Size_of_Largest_Community'], color='g', label='Size of Largest Community')
    for i, txt in enumerate(df['Louvian_Largest_Community_ID']):
        axes[0].annotate(txt, (df.index[i], df['Louvian_Largest_Community_ID'][i]))
    for i, txt in enumerate(df['Louvian_Size_of_Largest_Community']):
        axes[0].annotate(txt, (df.index[i], df['Louvian_Size_of_Largest_Community'][i]))
    axes[0].set_title('Louvian Community Detection Over Time')
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