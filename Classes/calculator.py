from Functions.operations import perform_operation
from Functions.validation import validate_operator, validate_numbers
from Logs.history import log_calculation


class Calculator:
    def __init__(self, decimal_places=2):
        self.memory = 0.0
        self.decimal_places = decimal_places  # Додаємо атрибут для кількості десяткових знаків
        self.history = []

    def get_user_input(self):
        """Отримує введення користувача для операції або команд."""
        first_number = input("Введіть перше число або 'm' для використання збереженого результату: ")
        if first_number == 'm':
            first_number = self.memory
        else:
            first_number = validate_numbers(first_number)

        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        validate_operator(operator)

        second_number = None
        if operator != '√':  # Квадратний корінь не потребує другого числа
            second_number = input("Введіть друге число або 'm' для використання збереженого результату: ")
            if second_number == 'm':
                second_number = self.memory
            else:
                second_number = validate_numbers(second_number)

        return first_number, operator, second_number

    def calculate(self):
        while True:
            try:
                first_number, operator, second_number = self.get_user_input()

                # Виконання операції
                result = perform_operation(first_number, operator, second_number)

                # Збереження результату в пам'ять
                self.memory = result

                # Додавання результату до історії
                log_calculation(first_number, second_number, operator, result)

                print(f"Result: {round(result, self.decimal_places)}")

                if input("Чи хочете продовжити? (y/n): ").lower() != 'y':
                    break

            except Exception as e:
                print(f"Помилка: {e}")

    def set_decimal_places(self, places):
        """Метод для встановлення кількості десяткових знаків."""
        self.decimal_places = places
        print(f"Decimal places set to: {self.decimal_places}")

