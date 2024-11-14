from Data.SPL_Lab1.calc import CCalculator
from Shared.Functions.history_functions import log_history, view_history, clear_history
from Shared.Functions.memory_functions import memory_save, memory_recall, memory_clear
from Data.SPL_Lab1.user_settingsLab1 import format_result, settings, set_decimal_places, toggle_auto_memory_save, \
    toggle_auto_memory_clear


def calculator():
    calc = CCalculator()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (в€љx)")
    print("7. Remainder (x % y)")
    print("M+. Memory Save")
    print("MR. Memory Recall")
    print("MC. Memory Clear")
    print("H. View History")
    print("CH. Clear History")
    print("S1. Set Decimal Places")
    print("S2. Toggle Auto Memory Save")
    print("S3. Toggle Auto Memory Clear")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/M+/MR/MC/H/CH/S1/S2/S3): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice == '6':
                num = float(input("Enter number for square root (в€љ): "))
                result = calc.sqrt(num)
                formatted_result = format_result(result)
                print(f"в€љ{num} = {formatted_result}")
                log_history(f"в€љ{num}", formatted_result)
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"{num1} + {num2} = {format_result(result)}")
                    log_history(f"{num1} + {num2}", format_result(result))
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"{num1} - {num2} = {format_result(result)}")
                    log_history(f"{num1} - {num2}", format_result(result))
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"{num1} * {num2} = {format_result(result)}")
                    log_history(f"{num1} * {num2}", format_result(result))
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    print(f"{num1} / {num2} = {format_result(result)}")
                    log_history(f"{num1} / {num2}", format_result(result))
                elif choice == '5':
                    result = calc.exponentiate(num1, num2)
                    print(f"{num1} ^ {num2} = {format_result(result)}")
                    log_history(f"{num1} ^ {num2}", format_result(result))
                elif choice == '7':
                    result = calc.remainder(num1, num2)
                    print(f"{num1} % {num2} = {format_result(result)}")
                    log_history(f"{num1} % {num2}", format_result(result))

            if settings["auto_memory_save"]:
                memory_save(format_result(result))

        elif choice == 'M+':
            if 'result' in locals():
                memory_save(format_result(result))
            else:
                print("No result to save.")
        elif choice == 'MR':
            recalled_value = memory_recall()
            if recalled_value is not None:
                print(f"Recalled value: {recalled_value}")
        elif choice == 'MC':
            memory_clear()
        elif choice == 'H':
            view_history()
        elif choice == 'CH':
            clear_history()
        elif choice == 'S1':
            set_decimal_places()
        elif choice == 'S2':
            toggle_auto_memory_save()
        elif choice == 'S3':
            toggle_auto_memory_clear()
        else:
            print("Invalid input, please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    if settings["auto_memory_clear"]:
        memory_clear()

if __name__ == '__main__':
    calculator()