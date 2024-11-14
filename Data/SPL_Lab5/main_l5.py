import colorama
from colorama import Fore, Back, Style
import math
from UI.Menu.cube_menu import display_menu


colorama.init()

# Global variables for cube settings
cube_width = 40
cube_height = 30
face_colors = {
    'top': Fore.RED,
    'left': Fore.GREEN,
    'right': Fore.BLUE,
    'bottom': Fore.YELLOW,
    'shadow': Fore.BLACK,
    'default': Fore.WHITE
}
light_direction = (-1, 1)  # Light source direction (x, y)


def apply_lighting(v1, v2):
    """ Calculate brightness based on the light source """
    dx = v2[0] - v1[0]
    dy = v2[1] - v1[1]
    dot_product = dx * light_direction[0] + dy * light_direction[1]

    # Normalize brightness to range [-1, 1]
    magnitude = math.sqrt(dx ** 2 + dy ** 2)
    if magnitude == 0:
        return 1  # No change if points are the same
    brightness = dot_product / magnitude

    # Map brightness to ASCII characters for shading
    if brightness > 0.7:
        return '#'
    elif brightness > 0.4:
        return '+'
    elif brightness > 0.1:
        return '.'
    else:
        return ' '


def draw_colored_cube(width, height, face_colors):
    cube = [[' '] * width for row in range(height)]
    vertices = {
        'tc': (width // 2, 0),
        'tl': (0, int(.25 * height)),
        'tr': (width - 1, int(.25 * height)),
        'cc': (width // 2, int(.5 * height)),
        'bl': (0, int(.75 * height)),
        'br': (width - 1, int(.75 * height)),
        'bc': (width // 2, height - 1)
    }

    # Define edges with colors for different faces and shading
    edges = {
        ('tc', 'tl'): face_colors['top'],
        ('tc', 'tr'): face_colors['top'],
        ('tl', 'cc'): face_colors['left'],
        ('tl', 'bl'): face_colors['left'],
        ('tr', 'cc'): face_colors['right'],
        ('tr', 'br'): face_colors['right'],
        ('bl', 'bc'): face_colors['bottom'],
        ('br', 'bc'): face_colors['bottom'],
        ('cc', 'bc'): face_colors['bottom'],
        ('tl', 'bl'): face_colors['shadow'],  # Shadow edge
        ('tr', 'br'): face_colors['shadow'],  # Shadow edge
    }

    for edge, color in edges.items():
        v1 = vertices[edge[0]]
        v2 = vertices[edge[1]]
        x1 = v1[0]
        y1 = v1[1]
        x2 = v2[0]
        y2 = v2[1]
        if x1 > x2:  # Always moving left to right
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        try:
            m = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            for yy in range(min(y1, y2), max(y1, y2)):
                cube[yy][x1] = color + apply_lighting(v1, v2) + Style.RESET_ALL
        else:
            yy = y1
            for xx in range(x1, x2):
                cube[int(yy)][xx] = color + apply_lighting(v1, v2) + Style.RESET_ALL
                yy += m

    cube_str = '\n'.join(''.join(row) for row in cube)
    return cube_str


def change_size():
    global cube_width, cube_height
    cube_width = int(input("Enter new cube width: "))
    cube_height = int(input("Enter new cube height: "))
    print(f"Cube size updated to {cube_width}x{cube_height}")


def assign_color_to_faces():
    global face_colors
    face = input("Choose face (top, left, right, bottom, shadow): ").strip().lower()
    color_choice = input("Choose a color (red, green, blue, yellow, white, black): ").strip().lower()

    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        'yellow': Fore.YELLOW,
        'white': Fore.WHITE,
        'black': Fore.BLACK
    }

    if face in face_colors and color_choice in color_map:
        face_colors[face] = color_map[color_choice]
        print(f"{face.capitalize()} face color updated to {color_choice.capitalize()}")
    else:
        print("Invalid face or color")


def adjust_light_source():
    global light_direction
    lx = int(input("Enter light source x-direction (-1 for left, 1 for right): "))
    ly = int(input("Enter light source y-direction (-1 for top, 1 for bottom): "))
    light_direction = (lx, ly)
    print(f"Light direction updated to {light_direction}")


def main5():
    while True:
        display_menu()
        choice = input("\nSelect an option: ")

        if choice == '1':
            change_size()
        elif choice == '2':
            assign_color_to_faces()
        elif choice == '3':
            adjust_light_source()
        elif choice == '4':
            print(draw_colored_cube(cube_width, cube_height, face_colors))
        elif choice == '5':
            print("Exiting Cube Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
