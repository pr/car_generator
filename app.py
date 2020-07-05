from flask import Flask, send_file
import subprocess

flask_app = Flask(__name__)


@flask_app.route('/')
def get_image():
    subprocess.call('main.py', shell=True)
    return send_file('app/car.png', mimetype='image/png')


if __name__ == "__main__":
    flask_app.run()
