from mailbox import Message
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess
import json
import shutil
from flask import jsonify
# import xray
import tempfile
import os,sys
sys.path.insert(0,"..")
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import argparse
import skimage, skimage.io
import pprint

import torch
import torch.nn.functional as F
import torchvision, torchvision.transforms

import torchxrayvision as xrv
app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = "/home/input"
transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop()])
model = xrv.models.get_model("densenet121-res224-all")
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


def predictCXR(filename):
    

    img = skimage.io.imread(filename)
    img = xrv.datasets.normalize(img, 255)  

    # Check that images are 2D arrays
    if len(img.shape) > 2:
        img = img[:, :, 0]
    if len(img.shape) < 2:
        print("error, dimension lower than 2 for image")

    # Add color channel
    img = img[None, :, :]

    transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop()])

    img = transform(img)


    model = xrv.models.get_model("densenet121-res224-all")

    output = {}
    with torch.no_grad():
        img = torch.from_numpy(img).unsqueeze(0)
        
        img = img.cuda()
        model = model.cuda()
            
        

        preds = model(img).cpu()
        output["preds"] = dict(zip(xrv.datasets.default_pathologies,preds[0].detach().numpy()))
        return output


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
            file.save(os.path.join("/tmp", filename))
            output = predictCXR(os.path.join("/tmp", filename))
            

        print(output)

        return json.dumps(str(output))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False,threaded=True)
