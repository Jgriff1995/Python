class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on.")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off.")
        else:
            print(f"Microwave ({self.brand}) is already turned off.")

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Running ({self.brand}) for {seconds} seconds.")
        else:
            print(f"Turn on Microwave first!")

    def __add__(self, other):
        return f"{self.brand} + {other.brand}"

    def __mul__(self, other):
        return f"{self.brand} * {other.brand}"

    def __str__(self) -> str:
        return f"{self.brand} (Rating: {self.power_rating})"

    def __repr__(self) -> str:
        return f"Microwave(Brand = {self.brand}, Power Rating = {self.power_rating})"


smeg: Microwave = Microwave("Smeg", "B")
bosch: Microwave = Microwave("Bosch", "C")

print(repr(smeg))
