from datetime import date
class Pig():
    def __init__(self, name, specie, shift ):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.shift = shift