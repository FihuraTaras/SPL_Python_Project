

#cli_interface.py
from Shared.Classes.ascii_art_generator import ASCIIArtGenerator

def preview_art(generator): #Завдання 9: Функція попереднього перегляду
    art = generator.generate_art()
    print(art)

