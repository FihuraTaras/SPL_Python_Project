from Shared.Classes.calculator import Calculator
from Shared.Logs.history import show_history, clear_history

def perform_calculation(calc):
    calc.calculate()

def view_history(_):
    show_history()

def use_memory(calc):
    if calc.memory:
        print(f"Memory value: {calc.memory}")
    calc.memory = float(input("Enter a value to store in memory: "))

def clear_calc_history(_):
    clear_history()

def exit_calculator(_):
    print("Exiting the calculator.")
    exit()

def set_decimal_places(calc):
    try:
        places = int(input("Enter the number of decimal places: "))
        calc.set_decimal_places(places)
    except ValueError:
        print("Invalid input. Please enter an integer.")

options = {
    '1': perform_calculation,
    '2': view_history,
    '3': use_memory,
    '4': clear_calc_history,
    '6': exit_calculator,
    '5': set_decimal_places
}

def main2():
    calc = Calculator()

    while True:
        print("\n1. Perform a calculation")
        print("2. View calculation history")
        print("3. Use memory")
        print("4. Clear history")
        print("5. Change decimal places")
        print("6. Exit")
       # print("6. Change decimal places")

        choice = input("Select an option: ")

        action = options.get(choice)
        if action:
            action(calc)
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main2()
