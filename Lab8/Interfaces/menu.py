# main.py
from Data.Lab8.Classes.DataProcessor import DataProcessor
from Data.Lab8.Classes.Visualizer import Visualizer
from Data.Lab8.Constants.config import CSV_FILE_PATH, IMAGE_FILE_PATH

def main8():
    # Load and preprocess data
    data_processor = DataProcessor(CSV_FILE_PATH)
    data_processor.preprocess_data()

    # Identify extremes for a column
    extremes = data_processor.identify_extremes('Sales_Amount')
    print(f"Extreme values for Sales_Amount: {extremes}")

    # Get processed data
    data = data_processor.get_data()

    # Create visualizations
    visualizer = Visualizer(data)
    visualizer.plot_basic_chart('Sales_Amount')
    visualizer.save_interactive_chart('Sales_Amount', IMAGE_FILE_PATH)




