from Classes.calculator import Calculator
from Logs.history import show_history

def main():
    calc = Calculator()

    while True:
        print("\n1. Perform a calculation")
        print("2. View calculation history")
        print("3. Change decimal places")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            calc.calculate()
        elif choice == '2':
            show_history()
        elif choice == '3':
            calc.change_decimal_places()
        elif choice == '4':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
