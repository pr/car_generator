import random
from io import BytesIO

from cars.boxy import Boxy
from cars.midsize import Midsize
from cars.race import Race
from window import Window

tile_size = 20

colors = ["red", "blue", "yellow", "purple", "orange", "green", "white", "black", "grey"]
color_selection = random.sample(colors, 4)
cars = [Boxy(color_selection), Midsize(color_selection), Race(color_selection)]

app = Window(random.choice(cars).picture, tile_size)

output = BytesIO()
app.result.save(output, 'PNG')
output.seek(0)

print(output.read())
