def log_calculation(num1, num2, operator, result):
    with open("Logs/calculation_history.txt", "a") as log_file:
        log_file.write(f"{num1} {operator} {num2} = {result}\n")

def show_history():
    try:
        with open("Logs/calculation_history.txt", "r") as log_file:
            history = log_file.readlines()
            for line in history:
                print(line.strip())
    except FileNotFoundError:
        print("No calculation history found.")
