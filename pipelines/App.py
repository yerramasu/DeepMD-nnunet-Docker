from mailbox import Message
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess
import json
import shutil
from flask import jsonify
import tempfile


app=Flask(__name__)

images = request.files.getlist('images')
files = []
for image in images:
    files.append(("images", (image.filename, image.read(), image.content_type)))
r = requests.post(url="http://example.com/post", data={"formdata1": "strvalue", "formdata2": "strvalue2"}, files=files)