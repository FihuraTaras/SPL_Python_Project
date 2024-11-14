# Classes/DataProcessor.py
import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def preprocess_data(self):
        # Basic data cleaning and handling of NaN values
        self.data.dropna(inplace=True)

    def identify_extremes(self, column):
        max_value = self.data[column].max()
        min_value = self.data[column].min()
        return {'max': max_value, 'min': min_value}

    def get_data(self):
        return self.data
