import math

def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '√':
        return math.sqrt(num1)
    else:
        raise ValueError(f"Unsupported operator: {operator}")
