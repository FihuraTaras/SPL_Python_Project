# Interfaces/IVisualizer.py
from abc import ABC, abstractmethod

class IVisualizer(ABC):
    @abstractmethod
    def plot_basic_chart(self, column):
        pass

    @abstractmethod
    def save_interactive_chart(self, column, file_name):
        pass
