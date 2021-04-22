from datetime import date

class Goat():
    def __init__(self, name, species, shift, food, chip_number):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.chip_number = chip_number

    def feed(self):
        print(f'{self.name} ate {self.food} at {date.today().strftime("%m/%d/%Y")}')
    
    @property
    def chip_number(self):
        return self.__chip_number # Note there are 2 underscores here
      


    @chip_number.setter
    def chip_number(self, number):
        pass
