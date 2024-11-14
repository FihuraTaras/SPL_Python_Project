def validate_numbers(num, operator=None):
    try:
        num = float(num)
        if operator == '√' and num < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return num
    except ValueError:
        raise ValueError("Invalid number entered.")

def validate_operator(operator):
    if operator not in ['+', '-', '*', '/', '%', '^', '√']:
        raise ValueError("Invalid operator. Please use +, -, *, /, %, ^, or √.")
    return operator