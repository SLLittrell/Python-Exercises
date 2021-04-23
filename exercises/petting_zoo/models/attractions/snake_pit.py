from .attraction import Attraction
class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    @property
    def last_critter_added(self):
        return self.animals[-1]