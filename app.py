import numpy as np
import os
import pandas as pd
from flask import Flask, redirect, request, render_template, url_for, flash
from werkzeug.utils import secure_filename
from tensorflow import keras



UPLOAD_FOLDER = 'uploads/predict'
ALLOWED_EXTENSIONS = {'jpg'}

app = Flask(__name__)
app.secret_key = 'wb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = keras.models.load_model('./models/model')


cls_long = [
        'Actinic keratosis or intraepithelial carcinoma',
        'Basal cell carcinoma',
        'Benign keratosis-like lesion',
        'Dermatofibroma',
        'Melanoma',
        'Melanocytic nevus',
        'Vascular lesion'
]



def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def series_creator(prediction:list) -> pd.Series(dtype=float):
    dict = {}
    for per, cl in zip(prediction, cls_long):
        dict[cl] = per
    return pd.Series(dict)

ser_0 = series_creator([0,0,0,0,0,0,0])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', v=ser_0, t='Upload your picture')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', v=ser_0, t = 'No file was found. Please upload a picture')
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html', v=ser_0, t = 'No file was found. Please upload a picture')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            im = keras.preprocessing.image_dataset_from_directory('./uploads', image_size=(180, 180))
            ser_1 =series_creator(np.round(model.predict(im)*100).ravel())
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', v = ser_1.sort_values(ascending=False))
        return render_template('index.html', v=ser_0, t = 'Please upload a picture in .jpg format')


if __name__ == "__main__":
    # You want to put the value of the env variable PORT if it exist (some services only open specifiques ports)
    port = int(os.environ.get("PORT", 4000))
    # Threaded option to enable multiple instances for
    # multiple user access support
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(debug=True, host="0.0.0.0", threaded=True, port=port)