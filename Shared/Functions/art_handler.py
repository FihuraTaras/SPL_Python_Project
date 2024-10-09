
#art_handler.py
import pyfiglet

def list_fonts(): #Завдання 3: Вибір шрифту
    fonts = pyfiglet.FigletFont.getFonts()  # Отримати всі доступні шрифти
    for i, font in enumerate(fonts, 1):
        print(f"{i}. {font}")
    return fonts

def choose_font(fonts, font_choice):
    try:
        font_index = int(font_choice) - 1
        if 0 <= font_index < len(fonts):
            return fonts[font_index]
        else:
            print("Invalid font choice. Using default font.")
            return 'slant'
    except ValueError:
        print("Invalid input. Using default font.")
        return 'slant'

