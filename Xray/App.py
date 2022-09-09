from mailbox import Message
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess
import json
import shutil
from flask import jsonify
import xray
import tempfile
app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = "/home/input"
# os.path.join(path, 'uploads')

# Make directory if uploads is not exists
# if not os.path.isdir(UPLOAD_FOLDER):
#     os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['dcm',  'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/cxr/predict', methods=['GET'])
def upload_form():
    return render_template('upload.html')

@app.route('/cxr')
def home():
  filename = 'info.json'
#   os.path.join(app.static_folder, 'info.json')
  message = ""
  with open(filename) as info_file:
        message = json.load(info_file)
#   message = "Kidney and Kidney Tumor Segmentation Challenge." +" Segmentation targets kidney and kidney tumors," +"Input modalities are 0: abdominal CT scan.  \n"
  return jsonify(message)

@app.route('/cxr/predict', methods=['POST'])
def upload():
    shutil.rmtree(app.config['UPLOAD_FOLDER'], ignore_errors=True)
    # os.mkdir(app.config['UPLOAD_FOLDER'])
    output = {}
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            filename = secure_filename(file.filename)
            print(filename)
            temp_dir = tempfile.TemporaryDirectory()
            file.save(os.path.join(temp_dir, filename))
            output = xray.predict(os.path.join(temp_dir, filename))
            

        
        return output


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False,threaded=True)
