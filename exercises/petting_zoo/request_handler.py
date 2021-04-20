from models import (Goat, Llama, Snake, Fish)
doodles = Llama('Doodles', 'llama', 'morning', 'Llama bits')
print(f'{doodles.name} the {doodles.species} is available to pet during the {doodles.shift} shift.')

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )

print(miss_fuzz.feed())
glenn = Goat('Glenn', 'nigerian', 'afternoon', 'hay')
print(glenn.feed())

bubbles = Fish('Bubbles', 'parana')
print(bubbles)