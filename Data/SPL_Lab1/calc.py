import math

class CCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero is undefined."
        return x / y

    def exponentiate(self, x, y):
        return x ** y

    def sqrt(self, x):
        if x < 0:
            return "Error: Square root of a negative number is undefined."
        return math.sqrt(x)

    def remainder(self, x, y):
        if y == 0:
            return "Error: Division by zero is undefined."
        return x % y
