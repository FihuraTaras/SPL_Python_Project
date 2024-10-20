# #ascii_art_generator.py
# import pyfiglet #Завдання 2: Бібліотека ASCII-арту
# #Абстракція
# class ASCIIArtGenerator: #атрибути t, f, c i методи для роботи з ними. Дозволяє керувати внутрішньою логікою генерації ASCII-арту без прямого доступу до атрибутів.
#     def __init__(self, text, font='slant', color='reset'):
#         self.text = text
#         self.font = font
#         self.color = color
#     def generate_art(self):
#
#         figlet = pyfiglet.Figlet(font=self.font)
#         ascii_art = figlet.renderText(self.text)
#         return self.apply_color(ascii_art, self.color)
#
#     def generate_art_with_size(self, width): #Завдання 7: Розмір ARTу
#         figlet = pyfiglet.Figlet(font=self.font, width=width)
#         ascii_art = figlet.renderText(self.text)
#         return self.apply_color(ascii_art, self.color)
#
#     def save_to_file(self, file_path, art): #Завдання 6: Збереження у файл
#         with open(file_path, 'w') as f:
#             f.write(art)
#
#     def apply_color(self, ascii_art, color):
#         color_codes = {
#             'red': '\033[31m',
#             'green': '\033[32m',
#             'blue': '\033[34m',
#             'yellow': '\033[33m',
#             'magenta': '\033[35m',
#             'cyan': '\033[36m',
#             'white': '\033[37m',
#             'black': '\033[30m',
#             'reset': '\033[0m'
#         }
#
#         if color in color_codes:
#             return f"{color_codes[color]}{ascii_art}{color_codes['reset']}"
#         else:
#             return ascii_art
#
from Shared.Fonts.ascii_font_library import get_font

class ASCIIArtGenerator:
    def __init__(self, text, symbol='*', color='', width=80, height=10, alignment='left'):
        self.text = text.upper()
        self.symbol = symbol
        self.color = color
        self.width = width
        self.height = height
        self.alignment = alignment
        self.font = get_font()

    def apply_color(self, text):
        """Застосовує ANSI-код для кольору."""
        colors = {
            'red': '\033[31m',
            'green': '\033[32m',
            'blue': '\033[34m',
            'reset': '\033[0m'
        }
        return f"{colors.get(self.color, colors['reset'])}{text}{colors['reset']}"

    def align_text(self, line):
        """Вирівнює текст залежно від обраного параметра."""
        if self.alignment == 'center':
            return line.center(self.width)
        elif self.alignment == 'right':
            return line.rjust(self.width)
        return line.ljust(self.width)

    def generate_art(self):
        """Генерує ASCII-арт із обраного тексту та застосовує вибрані параметри."""
        art_lines = [''] * len(next(iter(self.font.values())))

        for char in self.text:
            if char in self.font:
                char_lines = self.font[char]
                for i, line in enumerate(char_lines):
                    art_lines[i] += line.replace('#', self.symbol) + '  '
            else:
                for i in range(len(art_lines)):
                    art_lines[i] += ' ' * 6

        # Застосування вирівнювання та кольору
        aligned_art = [self.align_text(line[:self.width]) for line in art_lines[:self.height]]
        return '\n'.join(aligned_art)

    def save_to_file(self, file_path):
        """Зберігає ASCII-арт у файл без кольору."""
        art = self.generate_art()
        with open(file_path, 'w') as file:
            file.write(art)
        print(f"ASCII Art saved to {file_path}")
