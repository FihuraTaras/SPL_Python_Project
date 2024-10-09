

#menu builder
from Shared.Classes.ascii_art_generator import ASCIIArtGenerator
from Shared.Functions.art_handler import list_fonts, choose_font

def menu(): #Завдання 10: Інтерфейс, зрозумілий для користувача
    text = None
    generator = None
    selected_font = 'slant'
    selected_color = 'reset'

    while True:
        print("\n--- ASCII Art Generator Menu ---")
        print("1. Generate ASCII Art")
        print("2. Choose Font")
        print("3. Apply Color")
        print("4. Save to File")
        print("5. Preview Art")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            text = input("Enter text for ASCII Art: ") #Завдання 1: Введення користувача
            generator = ASCIIArtGenerator(text, selected_font, selected_color)
            art = generator.generate_art()
            print(art)

        elif choice == '2':
            fonts = list_fonts()
            font_choice = input("Choose font by number: ")
            selected_font = choose_font(fonts, font_choice)
            if text:
                generator = ASCIIArtGenerator(text, selected_font, selected_color)
                art = generator.generate_art()
                print(art)

        elif choice == '3':
            color = input("Choose color (red, green, blue, etc.): ")
            selected_color = color
            if generator:
                generator.color = selected_color
                art = generator.generate_art()
                print(art)
            else:
                print("Generate art first (option 1).")

        elif choice == '4':
            if generator:
                art = generator.generate_art()
                generator.save_to_file('Data/SPL_Lab3/ascii_art.txt', art)
                print(f"Art saved to Data/SPL_Lab3/ascii_art.txt")
            else:
                print("Generate art first (option 1).")

        elif choice == '5':
            if generator:
                print("Previewing art:")
                art = generator.generate_art()
                print(art)
            else:
                print("Generate art first (option 1).")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")
