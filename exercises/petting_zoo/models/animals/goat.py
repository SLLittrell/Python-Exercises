from datetime import date
from .animals import Animal

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species,food, chip_num)
        self.walking = True
        self.shift = shift
