import os

def save_to_file(file_path, art):
    with open(file_path, 'w') as f:
        f.write(art)
    print(f"Art saved to {file_path}")

def get_user_input(prompt, default=None):
    value = input(prompt)
    return value if value else default

def preview_art(art):
    print("\n--- Preview of your ASCII Art ---")
    print(art)
