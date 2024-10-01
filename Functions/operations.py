import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b

def power(a, b):
    return a ** b

def square_root(a, _):
    if a < 0:
        raise ValueError("Не можна обчислити квадратний корінь з від'ємного числа")
    return math.sqrt(a)

def modulus(a, b):
    return a % b

# Словник для вибору функції
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power,
    '√': square_root,
    '%': modulus,
}

def perform_operation(a, operator, b):
    """Виконує операцію, базуючись на виборі оператора."""
    operation = operations.get(operator)
    if not operation:
        raise ValueError(f"Оператор {operator} не підтримується")
    return operation(a, b)

