class PettingZoo():
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)