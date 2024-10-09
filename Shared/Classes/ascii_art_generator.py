#ascii_art_generator.py
import pyfiglet #Завдання 2: Бібліотека ASCII-арту
#Абстракція
class ASCIIArtGenerator: #атрибути t, f, c i методи для роботи з ними. Дозволяє керувати внутрішньою логікою генерації ASCII-арту без прямого доступу до атрибутів.
    def __init__(self, text, font='slant', color='reset'):
        self.text = text
        self.font = font
        self.color = color
    def generate_art(self):

        figlet = pyfiglet.Figlet(font=self.font)
        ascii_art = figlet.renderText(self.text)
        return self.apply_color(ascii_art, self.color)

    def generate_art_with_size(self, width): #Завдання 7: Розмір ARTу
        figlet = pyfiglet.Figlet(font=self.font, width=width)
        ascii_art = figlet.renderText(self.text)
        return self.apply_color(ascii_art, self.color)

    def save_to_file(self, file_path, art): #Завдання 6: Збереження у файл
        with open(file_path, 'w') as f:
            f.write(art)

    def apply_color(self, ascii_art, color):
        color_codes = {
            'red': '\033[31m',
            'green': '\033[32m',
            'blue': '\033[34m',
            'yellow': '\033[33m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'black': '\033[30m',
            'reset': '\033[0m'
        }

        if color in color_codes:
            return f"{color_codes[color]}{ascii_art}{color_codes['reset']}"
        else:
            return ascii_art