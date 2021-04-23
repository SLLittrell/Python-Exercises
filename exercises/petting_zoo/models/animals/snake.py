from datetime import date
class Snake():
    def __init__(self, name, species, food ):
        self.name = name
        self.species = name
        self.date_added = date.today()
        self.slithering = True
        self.food = food


    def feed(self):
        return f'Fed {self.food} on {date.today().strftime("%m/%d/%Y")}'