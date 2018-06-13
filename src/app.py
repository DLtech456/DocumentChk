import os
from flask import Flask, render_template, request
from src.models.processdata import ImageDetect

app = Flask(__name__)


UPLOAD_FOLDER = os.path.join('static','uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

