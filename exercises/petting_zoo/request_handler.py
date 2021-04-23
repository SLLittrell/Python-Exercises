from models import (Goat, Llama, Snake, Fish, Goose)
from models import (PettingZoo, SnakePit, Wetland, Attraction)

# glenn = Goat('Glenn', 'nigerian')
# kuzco = Llama('Kuzco', 'demestic')
# bubbles = Fish('Bubbles', 'parana')
# fang = Snake('Fang', ' Corn snake' )
# penelope = Pig('Penelope', 'Popbellied')
# bunkie = Cat('Bunkie', 'tabby')
# rough = Dog('Rough', 'Lab')
# shy = Sheep()
# nah = Horse()
# leo = Lizard()


doodles = Llama('Doodles', 'llama', 'morning', 'Llama bits', 24678)
# print(f'{doodles.name} the {doodles.species} is available to pet during the {doodles.shift} shift.')

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 12345 )

# print(miss_fuzz.feed())
glenn = Goat('Glenn', 'nigerian', 'afternoon', 'hay', 55509)
# print(glenn.feed())

bubbles = Fish('Bubbles', 'parana')
# print(bubbles)

fuzz = miss_fuzz.name
bites = PettingZoo('Bites', 'watch out')
bites.add_animal(fuzz)
# print(f'{bites.description} for {bites.animals[0]} at the {bites.attraction_name} Petting Zoo')

glenn.chip_number = 30119
# print(glenn.chip_number)
fang = Snake('Fang', ' Corn snake', 'mice')
tom = Snake('Tom', 'Ball Python', 'mice')

# print(fang.feed())
slytherin = SnakePit('Slytherin', 'Cuddle up with us')
slytherin.add_animal(fang.name)
slytherin.add_animal(tom.name)

# print(f'animals in {slytherin.attraction_name}:{slytherin.animals}')


print(slytherin.last_critter_added)

# print(int(glenn.chip_number))

stinky = Goat("Stinky", "domestic goat", "afternoon", "barley hay", 45678)

# print(f"{doodles.feed()}")

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 45638)

# Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)
