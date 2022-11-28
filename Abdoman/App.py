from mailbox import Message
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess
import json
import shutil
from flask import jsonify, send_file
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
ALLOWED_EXTENSIONS = set(['dcm', 'nii.gz', 'dicom', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/abdoman/predict', methods=['GET'])
def upload_form():
    return render_template('upload.html')

@app.route('/abdoman')
def home():
  filename = 'info.json'
#   os.path.join(app.static_folder, 'info.json')
  message = ""
  with open(filename) as info_file:
        message = json.load(info_file)
#   message = "Kidney and Kidney Tumor Segmentation Challenge." +" Segmentation targets kidney and kidney tumors," +"Input modalities are 0: abdominal CT scan.  \n"
  return jsonify(message)

@app.route('/abdoman/predict', methods=['POST'])
def upload():
    print("inside ---")
    # os.mkdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':

        
        print("inside ---")
        files = request.files.getlist('files[]')
        inputDir = tempfile.mkdtemp()
        os.environ['inputDir'] = inputDir
        outDir = tempfile.mkdtemp()
        os.environ['outDir'] = outDir

        for file in files:
            filename = secure_filename(file.filename)
            print(filename)
            file.save("/home/input/" +filename)
            #file.save(os.path.join(inputDir), filename)
            # if file and allowed_file(file.filename):
            #     filename = secure_filename(file.filename)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # flash('File(s) successfully uploaded')
        # session = Popen(['./some.sh'], stdout=PIPE, stderr=PIPE)
        print(app.config['UPLOAD_FOLDER'])
        my = os.listdir(app.config['UPLOAD_FOLDER'])
        print("input dir = ",my)
        # subprocess.check_output("/home/predict.sh", shell=True)
        subprocess.check_output("/home/predict.sh", shell=True)
        # return outfile_0000.nii.gz

        # return redirect('/abdoman/predict')
        file_to_send = open("/home/output/infile.nii.gz", 'rb')
        # file_to_send = f.read()
        # return send_file(file_to_send, mimetype="application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip")
        return send_file("/home/output/infile.nii.gz", mimetype="application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip")

        

@app.route('/abdoman/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':

       

        
        subprocess.check_output("/home/predict.sh", shell=True)
        return redirect('/abdoman/test')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False,threaded=True)
