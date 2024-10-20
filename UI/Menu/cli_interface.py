# #cli_interface.py
# from Shared.Classes.ascii_art_generator import ASCIIArtGenerator
#
# def preview_art(generator): #Завдання 9: Функція попереднього перегляду
#     art = generator.generate_art()
#     print(art)

from Shared.Fonts.ascii_font_library import get_font

class ASCIIArtGenerator:
    def __init__(self, text, symbol='*'):
        self.text = text.upper()  # Приводимо текст до верхнього регістру для відповідності шрифту
        self.symbol = symbol
        self.font = get_font()

    def generate_art(self):
        """Генерує ASCII-арт із обраного тексту та символів."""
        art_lines = [''] * len(next(iter(self.font.values())))  # Порожні рядки для рядків шрифту

        for char in self.text:
            if char in self.font:
                char_lines = self.font[char]
                for i, line in enumerate(char_lines):
                    art_lines[i] += line.replace('#', self.symbol) + '  '
            else:
                for i in range(len(art_lines)):
                    art_lines[i] += ' ' * 6  # Пропуск для невідомих символів

        return '\n'.join(art_lines)
