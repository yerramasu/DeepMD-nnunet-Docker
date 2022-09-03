import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess

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


@app.route('/test')
def upload_form():
    return render_template('upload.html')

@app.route('/')
def home():
  message = "Multi-Atlas Labeling Beyond the Cranial Vault - Abdomen. \n" +"Segmentation targets are thirteen different abdominal organs, " +"Input modalities are 0: abdominal CT scan. "
  return message

@app.route('/test', methods=['POST'])
def upload():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # if file and allowed_file(file.filename):
            #     filename = secure_filename(file.filename)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # flash('File(s) successfully uploaded')
        # session = Popen(['./some.sh'], stdout=PIPE, stderr=PIPE)
        print(app.config['UPLOAD_FOLDER'])
        my = os.listdir(app.config['UPLOAD_FOLDER'])
        print("input dir = ",my)
        # subprocess.check_output("/home/predict.sh", shell=True)
        return redirect('/test')

@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':

       

        
        subprocess.check_output("/home/predict.sh", shell=True)
        return redirect('/test')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False,threaded=True)
