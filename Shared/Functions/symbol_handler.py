def choose_symbols():
    symbols_input = input("Enter characters to use for ASCII art, separated by spaces (e.g., @ # * .): ")
    symbols = symbols_input.split()
    if symbols:
        return symbols
    else:
        print("Invalid input. Using default symbols.")
        return ['@', '#', '*', '.', ' ']
