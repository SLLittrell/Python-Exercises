from models import (Goat, Llama, Snake)
doodles = Llama('Doodles', 'llama', 'morning')
print(f'{doodles.name} the {doodles.species} is available to pet during the {doodles.shift} shift.')