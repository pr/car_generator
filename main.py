from PIL import ImageTk
import random
from tkinter import Tk, Label

from cars.boxy import Boxy
from cars.midsize import Midsize
from cars.race import Race
from window import Window

tile_size = 20

root = Tk()

colors = ["red", "blue", "yellow", "purple", "orange", "green", "white", "black", "grey"]
color_selection = random.sample(colors, 4)
cars = [Boxy(color_selection), Midsize(color_selection), Race(color_selection)]

app = Window(random.choice(cars).picture, tile_size)
app.master = root

render = ImageTk.PhotoImage(app.result)
root.geometry(f"{app.side_length}x{app.side_length}")

filename = "car.png"
render._PhotoImage__photo.write(filename)
