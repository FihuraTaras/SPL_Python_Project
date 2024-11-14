from Shared.Interfaces.ccalculator import calculator
from Data.SPL_Lab2.runner_l2 import main2
from Data.SPL_Lab3.runner_l3 import menu
from Data.SPL_Lab5.runner_l5 import main5
from Data.SPL_Lab6.runner_l6 import run_weather_tests
from Data.SPL_Lab7.runner_l7 import main7
from UTest.Test2 import main8

def show_menu():
    print("\nMenu:")
    print("1. Lab 1")#
    print("2. Lab 2")#
    print("3. Lab 3")#
    print("4. Lab 4")
    print("5. Lab 5")#
    print("6. Lab 6")#
    print("7. Lab 7")#
    print("8. Lab 8")
    print("0. Exit")

def main():
    while True:
          show_menu()
          choice = input("Enter your choice (0 to exit): ")
          if choice == '1':
               calculator()
          elif choice == '2':
               main2()
          elif choice == '3':
               menu()
          elif choice == '4':
               menu()
          elif choice == '5':
               main5()
          elif choice == '6':
               run_weather_tests()
          elif choice == '7':
               main7()
          elif choice == '8':
               main8()
          elif choice == '0':
               print("Exiting the program.")
               break
          else:
               print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


