from mailbox import Message
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess
import json
import shutil
from flask import jsonify
import requests
import tarfile
import os.path
import time
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
ALLOWED_EXTENSIONS = set(['dcm', 'nii.gz', 'dicom', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/dicom/upload', methods=['GET'])
def upload_form():
    return render_template('upload.html')

@app.route('/dicom')
def home():
  filename = 'info.json'
#   os.path.join(app.static_folder, 'info.json')
  message = ""
  with open(filename) as info_file:
        message = json.load(info_file)
#   message = "Kidney and Kidney Tumor Segmentation Challenge." +" Segmentation targets kidney and kidney tumors," +"Input modalities are 0: abdominal CT scan.  \n"
  return jsonify(message)

@app.route('/dicom/upload', methods=['POST'])
def upload():
    
    if request.method == 'POST':


        files = request.files.getlist('files[]')
        # url = request.values.get('dicomURL')
        # print(url)
        # IsSend = request.values.get('IsSend')
        # print(IsSend)
        

        for file in files:
            filename = secure_filename(file.filename)
            # response = requests.post(url,data=file, headers={'Content-Type': 'application/octet-stream'},verify=False)
            # # print(response)
            # data = response.json()
            print(filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # if file and allowed_file(file.filename):
            #     filename = secure_filename(file.filename)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # subprocess.check_output("/home/pipeline.sh", shell=True)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        # return redirect('/dicom/upload')

@app.route('/dicom/upload/v2', methods=['POST'])
def uploadDICOM():
    
    if request.method == 'POST':


        files = request.files.getlist('files[]')
        
        url = "https://lab.deepmd.io/instances"
        for file in files:
            filename = secure_filename(file.filename)
            print(filename)
            response = requests.post(url,data=file, headers={'Content-Type': 'application/octet-stream'},verify=False)
            # print(response)
            data = response.json()
            print(data)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        # return redirect('/dicom/upload')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False,threaded=True)
