# Parent Image
FROM nvcr.io/nvidia/pytorch:20.10-py3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt install plastimatch

RUN cd /home
RUN mkdir /home/input
RUN mkdir /home/output

COPY pipeline.sh /home
COPY predict.sh /home
# COPY listdir.py /home
COPY App.py /home
COPY info.json /home
RUN mkdir /home/templates
COPY templates/upload.html /home/templates
# Installing nnU-Net
RUN pip install flask 
  
RUN chmod +x /home/pipeline.sh
RUN chmod +x /home/predict.sh
RUN cd /home
WORKDIR /home
ENV FLASK_APP=App.py
# RUN  /home/pipeline.sh 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]