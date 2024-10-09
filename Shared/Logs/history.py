import os

history_file = "Shared/Logs/calculation_history.txt"

def log_calculation(num1, num2, operator, result):
    with open(history_file, 'a') as f:
        if num2 is not None:
            f.write(f"{num1} {operator} {num2} = {result}\n")
        else:
            f.write(f"{operator}{num1} = {result}\n")

def show_history():
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = f.read()
        if history:
            print("Calculation History:\n", history)
        else:
            print("No history available.")
    else:
        print("No history available.")

def clear_history():
    if os.path.exists(history_file):
        os.remove(history_file)
        print("History file removed.")
    else:
        print("No history file found to remove.")

