# Functions/visualization.py
import matplotlib.pyplot as plt
import plotly.express as px

def plot_histogram(data, column):
    plt.hist(data[column], bins=10)
    plt.title(f'{column} Distribution')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_interactive_line(data, column, file_name):
    fig = px.line(data, y=column, title=f'{column} Over Time')
    fig.write_image(file_name)
