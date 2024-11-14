# Classes/Visualizer.py
import plotly.express as px

class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_basic_chart(self, column):
        fig = px.line(self.data, y=column, title=f'{column} Over Time')
        fig.show()

    def save_interactive_chart(self, column, file_name):
        fig = px.line(self.data, y=column, title=f'{column} Over Time')
        # Save as HTML if PNG export fails
        try:
            fig.write_image(file_name)
        except ValueError:
            print("PNG export failed, saving as HTML instead.")
            html_file_name = file_name.replace('.png', '.html')
            fig.write_html(html_file_name)
