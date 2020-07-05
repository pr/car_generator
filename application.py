import ast
import io
import subprocess

from flask import Flask, send_file

flask_app = Flask(__name__)


@flask_app.route('/')
def get_image():
    # car_png = subprocess.check_output('main.py', shell=True)
    #
    # print(car_png)
    #
    # return send_file(io.BytesIO(ast.literal_eval(car_png.decode("ascii"))), mimetype='image/png')

    return "hello?"


if __name__ == "__main__":
    flask_app.run()
