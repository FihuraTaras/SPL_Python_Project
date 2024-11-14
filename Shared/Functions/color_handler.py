#color_handler.py
from termcolor import colored

def is_color_supported():
    try:
        import os
        return os.name != 'nt' or 'ANSICON' in os.environ or 'WT_SESSION' in os.environ
    except ImportError:
        return False

def apply_color(text, color='white'): #Завдання 4: Колір тексту
    if is_color_supported():
        try:
            return colored(text, color)
        except KeyError:
            return colored(text, 'white')
    else:
        return text  # Якщо кольори не підтримуються, просто повертаємо текст без кольору


