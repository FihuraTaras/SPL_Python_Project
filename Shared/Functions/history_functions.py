# Functions/history_functions.py
from Data.SPL_Lab1.hhistory import history


def log_history(expression, result):
    history.append(f"{expression} = {result}")

def view_history():
    if history:
        print("\n--- Calculation History ---")
        for entry in history:
            print(entry)
    else:
        print("No history available.")

def clear_history():
    history.clear()
    print("Calculation history cleared.")