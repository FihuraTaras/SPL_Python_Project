from Functions.operations import perform_operation
from Functions.validation import validate_operator, validate_numbers
from Logs.history import log_calculation


class Calculator:
    def __init__(self, decimal_places=2):
        self.memory = None
        self.history = []
        self.decimal_places = decimal_places  # Number of decimal

    @staticmethod
    def get_user_input():
        num1 = input("Enter the first number (or 'm' to use memory): ")
        num2 = input("Enter the second number: ")
        operator = input("Enter the operator (+, -, *, /, %, ^, √): ")

        num1 = validate_numbers(num1)
        num2 = validate_numbers(num2, operator)
        operator = validate_operator(operator)

        return num1, num2, operator

    def calculate(self):
        while True:
            try:
                num1, num2, operator = self.get_user_input()

                if num1 == 'm':
                    if self.memory is None:
                        print("Memory is empty.")
                        continue
                    num1 = self.memory

                result = perform_operation(num1, num2, operator)

                # We format the result by the number of decimal places
                result = round(result, self.decimal_places)

                print(f"The result of {num1} {operator} {num2} is: {result}")
                log_calculation(num1, num2, operator, result)
                self.history.append((num1, num2, operator, result))

                if input("Save result to memory? (y/n): ").lower() == 'y':
                    self.memory = result

                if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
                    break
            except Exception as e:
                print(f"Error: {e}")

    def change_decimal_places(self):
        try:
            new_places = int(input("Enter the number of decimal places to display: "))
            if new_places >= 0:
                self.decimal_places = new_places
                print(f"Decimal places set to: {self.decimal_places}")
            else:
                print("Decimal places must be 0 or higher.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
