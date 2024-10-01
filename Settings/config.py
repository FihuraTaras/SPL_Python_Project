DECIMAL_PLACES = 2

class Config:
    def __init__(self):
        self.decimal_places = 2

    def set_decimal_places(self, places):
        try:
            places = int(places)
            if places >= 0:
                self.decimal_places = places
                print(f"Decimal places set to {places}")
            else:
                print("Decimal places cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
