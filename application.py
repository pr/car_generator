import io

from flask import Flask, send_file, render_template

import random
from io import BytesIO

from cars.boxy import Boxy
from cars.midsize import Midsize
from cars.race import Race
from car import Car

flask_app = Flask(__name__)


@flask_app.route('/')
def home():
    return render_template('index.html')


@flask_app.route('/generate')
def get_image():
    tile_size = 40

    colors = ["red", "blue", "yellow", "purple", "orange", "green", "white", "black", "grey"]
    color_selection = random.sample(colors, 4)
    cars = [Boxy(color_selection), Midsize(color_selection), Race(color_selection)]

    car = Car(random.choice(cars).picture, tile_size)

    output = BytesIO()
    car.result.save(output, 'PNG')
    output.seek(0)

    return send_file(io.BytesIO(output.read()), mimetype='image/png')


if __name__ == "__main__":
    flask_app.run()
