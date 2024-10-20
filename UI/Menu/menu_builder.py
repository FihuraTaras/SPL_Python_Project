# #menu builder
# from Shared.Classes.ascii_art_generator import ASCIIArtGenerator
# from Shared.Functions.art_handler import list_fonts, choose_font
#
# def menu(): #Завдання 10: Інтерфейс, зрозумілий для користувача
#     text = None
#     generator = None
#     selected_font = 'slant'
#     selected_color = 'reset'
#
#     while True:
#         print("\n--- ASCII Art Generator Menu ---")
#         print("1. Generate ASCII Art")
#         print("2. Choose Font")
#         print("3. Apply Color")
#         print("4. Save to File")
#         print("5. Preview Art")
#         print("6. Exit")
#
#         choice = input("Select an option: ")
#
#         if choice == '1':
#             text = input("Enter text for ASCII Art: ") #Завдання 1: Введення користувача
#             generator = ASCIIArtGenerator(text, selected_font, selected_color)
#             art = generator.generate_art()
#             print(art)
#
#         elif choice == '2':
#             fonts = list_fonts()
#             font_choice = input("Choose font by number: ")
#             selected_font = choose_font(fonts, font_choice)
#             if text:
#                 generator = ASCIIArtGenerator(text, selected_font, selected_color)
#                 art = generator.generate_art()
#                 print(art)
#
#         elif choice == '3':
#             color = input("Choose color (red, green, blue, etc.): ")
#             selected_color = color
#             if generator:
#                 generator.color = selected_color
#                 art = generator.generate_art()
#                 print(art)
#             else:
#                 print("Generate art first (option 1).")
#
#         elif choice == '4':
#             if generator:
#                 art = generator.generate_art()
#                 generator.save_to_file('Data/SPL_Lab3/ascii_art.txt', art)
#                 print(f"Art saved to Data/SPL_Lab3/ascii_art.txt")
#             else:
#                 print("Generate art first (option 1).")
#
#         elif choice == '5':
#             if generator:
#                 print("Previewing art:")
#                 art = generator.generate_art()
#                 print(art)
#             else:
#                 print("Generate art first (option 1).")
#
#         elif choice == '6':
#             print("Exiting the program.")
#             break
#
#         else:
#             print("Invalid option. Please try again.")

from Shared.Classes.ascii_art_generator import ASCIIArtGenerator

def menu():
    text = ''
    symbol = '*'
    color = 'reset'
    width, height = 80, 10
    alignment = 'left'

    while True:
        print("\n1. Enter Text for ASCII Art")
        print("2. Choose Symbol for ASCII Art")
        print("3. Choose Text Color")
        print("4. Set Width and Height")
        print("5. Set Text Alignment")
        print("6. Preview ASCII Art")
        print("7. Save ASCII Art to File")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            text = input("Enter the text: ")

        elif choice == '2':
            symbol = input("Enter the symbol to use (e.g., '@', '#', '*'): ")

        elif choice == '3':
            print("Available colors: red, green, blue")
            color = input("Enter the color: ").lower()

        elif choice == '4':
            width = int(input("Enter the width (max 100): "))
            height = int(input("Enter the height (max 20): "))
            width = min(max(10, width), 100)
            height = min(max(5, height), 20)

        elif choice == '5':
            print("Alignment options: left, center, right")
            alignment = input("Choose alignment: ").lower()

        elif choice == '6':
            if text:
                generator = ASCIIArtGenerator(text, symbol, color, width, height, alignment)
                art = generator.generate_art()
                print("\nPreview of ASCII Art:\n")
                print(generator.apply_color(art))
            else:
                print("Please enter text first.")

        elif choice == '7':
            if text:
                file_path = input("Enter file name (with .txt extension): ")
                generator = ASCIIArtGenerator(text, symbol, color, width, height, alignment)
                generator.save_to_file(file_path)
            else:
                print("Please enter text first.")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
