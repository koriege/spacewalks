import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_df(input_file):
    """
    data import and wrangling into a format able to be digested by pandas plot function
    includes NA removal and sorting

    Args:
        input_file (str): path to JSON file
    
    Returns:
        eva_df (pd.DataFrame): cleaned and sorted data frame 
    """
    print(f'reading file {input_file}')
    input_file = open(input_file, 'r')
    eva_df = pd.read_json(input_file, convert_dates=['date']) # loads in the raw data
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True) # removes NAs from data table
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_df_to_csv(eva_df, output_file):
    """
    write pandas data frame to csv file

    Args:
        eva_df (pd.DataFrame): data frame 
        output_file (str): path to csv file
    
    Returns:
        None
    """
    print(f'writing file {output_file}')
    output_file = open(output_file, 'w')
    eva_df.to_csv(output_file, index=False)


def plot_time_in_space(eva_df, output_file):
    """
    plot and save a cumulative graph of duration time in space

    Args:
        eva_df (pd.DataFrame): data frame 
        output_file (str): path to png file
    
    Returns:
        None
    """
    print(f'writing file {output_file}')
    # split the time format HH:MM into duration as hours
    eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
    plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = './eva-data.json'
output_file = './eva-data.csv', 'w'
graph_file = './cumulative_eva_graph.png'

eva_df = read_json_to_df(input_file)
write_df_to_csv(eva_df, output_file)
plot_time_in_space(eva_df, graph_file)

