# Parent Image
FROM nvcr.io/nvidia/pytorch:20.10-py3

RUN mkdir /home/models

# COPY listdir.py /home
COPY App.py /home
COPY xray.py /home
COPY info.json /home
RUN mkdir /home/templates
COPY templates/upload.html /home/templates
# Installing nnU-Net
RUN cd /home && \
  #mkdir /home/input && \
  #mkdir /home/output && \
  mkdir /home/xray && \
  pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113 && \
  pip install torchxrayvision && \
  pip install flask && \
  # git clone https://github.com/mlmed/torchxrayvision.git  && \
  # cp torchxrayvision/scripts/*py /home && \
  mkdir /home/xray/input && \
  cd /home 
  
  

RUN cd /home
WORKDIR /home
ENV FLASK_APP=App.py
# RUN  /home/pipeline.sh 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
