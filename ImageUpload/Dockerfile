# Parent Image
# FROM nvcr.io/nvidia/pytorch:20.10-py3
FROM python:3.8-slim-buster
# RUN  apt-get update && apt-get upgrade -y
# RUN  apt-get install -y wget
# RUN  apt-get install -y unzip
# RUN  apt install -y plastimatch
# RUN  apt install -y subversion
RUN cd /home
RUN mkdir /home/templates
RUN cp App.py /home
COPY templates/upload.html /home/templates

# RUN pip install nnunet
RUN pip install pydicom
RUN pip install flask
RUN pip install requests


# Installing nnU-Net
RUN cd /home
WORKDIR /home
ENV FLASK_APP=App.py
# RUN  /home/pipeline.sh 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
