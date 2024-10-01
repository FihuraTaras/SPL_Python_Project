from Classes.calculator import Calculator
from Logs.history import show_history, clear_history

def perform_calculation(calc):
    """Виконати обчислення."""
    calc.calculate()

def view_history(_):
    """Показати історію обчислень."""
    show_history()

def use_memory(calc):
    """Використати значення з пам'яті або зберегти нове."""
    if calc.memory:
        print(f"Memory value: {calc.memory}")
    calc.memory = float(input("Enter a value to store in memory: "))

def clear_calc_history(_):
    """Очистити історію."""
    clear_history()

def exit_calculator(_):
    """Вийти з калькулятора."""
    print("Exiting the calculator.")
    exit()

def set_decimal_places(calc):
    """Встановити кількість десяткових знаків для калькулятора."""
    try:
        places = int(input("Enter the number of decimal places: "))
        calc.set_decimal_places(places)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Словник, де ключі - вибрані користувачем опції, а значення - відповідні функції
options = {
    '1': perform_calculation,
    '2': view_history,
    '3': use_memory,
    '4': clear_calc_history,
    '6': exit_calculator,
    '5': set_decimal_places  # Додаємо опцію для зміни кількості десяткових знаків
}

def main():
    calc = Calculator()

    while True:
        print("\n1. Perform a calculation")
        print("2. View calculation history")
        print("3. Use memory")
        print("4. Clear history")
        print("5. Change decimal places")  # Новий пункт меню
        print("6. Exit")
       # print("6. Change decimal places")  # Новий пункт меню

        choice = input("Select an option: ")

        # Викликаємо відповідну функцію на основі вибору користувача
        action = options.get(choice)
        if action:
            action(calc)  # Передаємо калькулятор як аргумент, якщо потрібно
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
