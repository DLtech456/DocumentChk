import os
from flask import Flask, render_template, request
from src.models.processdata import ImageDetect

app = Flask(__name__)


UPLOAD_FOLDER = os.path.join('./src/static','uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filename)
    seValues = ImageDetect.SightEngineCall(filename)
    female = seValues[1]
    face = seValues[2]

    # obtain the OCR data
    ocr = ImageDetect.ocr_space_file(filename)
    p2 = ocr[1]
    dLicense=ocr[2]

    return render_template('uploaded.html', female=female, face=face, init=True, user_image=filename, ocr=p2,dLicense=dLicense)


if __name__ == "__main__":
    app.run()

