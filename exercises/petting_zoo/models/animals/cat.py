from datetime import date
class Cat():
    def __init__(self, name, species ):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True