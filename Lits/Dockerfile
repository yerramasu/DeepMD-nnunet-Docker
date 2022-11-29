# Parent Image
FROM nvcr.io/nvidia/pytorch:20.10-py3

# RUN apt-get update && apt-get upgrade -y
# RUN apt-get install -y wget
# RUN apt-get install -y unzip
# RUN pip3 install virtualenv 
# COPY env/ /env/
# RUN  source /env/bin/activate
ENV nnUNet_raw_data_base "/home/nnUNet/data/nnUNet_raw_data_base"
ENV nnUNet_preprocessed "/home/nnUNet/data/nnUNet_preprocessed"
ENV RESULTS_FOLDER "/home/nnUNet/data/models"
ENV seg_model_url  "https://www.dropbox.com/s/m7es2ojn8h0ybhv/Task055_SegTHOR.zip?dl=0"
ENV output_path  "/home/models/Task002_Heart.zip"
RUN mkdir /home/models
# RUN wget  -O /home/models/Task055_SegTHOR.zip https://www.dropbox.com/s/m7es2ojn8h0ybhv/Task055_SegTHOR.zip?dl=0
#-O $output_path $seg_model_url
# RUN mkdir /home/models
COPY  Task003_Liver.zip /home/models
COPY pipeline.sh /home
COPY predict.sh /home
# COPY listdir.py /home
COPY App.py /home
COPY info.json /home
RUN mkdir /home/templates
COPY templates/upload.html /home/templates
# Installing nnU-Net
RUN cd /home && \
  #mkdir /home/input && \
  #mkdir /home/output && \
  mkdir /home/nnUNet && \
  pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113 && \
  pip install nnunet && \
  pip install flask && \
  #git clone https://github.com/MIC-DKFZ/nnUNet.git  && \
  mkdir /home/nnUNet/input && \
#   mkdir /home/models && \
  mkdir /home/nnUNet/output && \
  mkdir /home/nnUNet/data && \
  mkdir /home/nnUNet/data/models && \
  mkdir /home/nnUNet/data/nnUNet_raw_data_base && \
  mkdir /home/nnUNet/data/nnUNet_preprocessed && \
  cd /home/nnUNet && \
  # pip install -e . && \
  #pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113 && \
  #pip install -e . && \
  #pip3 install progress && \
  #pip3 install graphviz && \
  # nnUNet_download_pretrained_model Task003_Liver &&  \
  nnUNet_install_pretrained_model_from_zip /home/models/Task003_Liver.zip   && \
  cd /home
RUN pip install flask_cors
RUN chmod +x /home/pipeline.sh
RUN chmod +x /home/predict.sh
RUN cd /home
WORKDIR /home
ENV FLASK_APP=App.py
# RUN  /home/pipeline.sh 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# ENTRYPOINT ["/home/pipeline.sh"]
# Installing additional libraries
# WORKDIR /workspace/
# RUN pip3 install --upgrade git+https://github.com/nanohanno/hiddenlayer.git@bugfix/get_trace_graph#egg=hiddenlayer
# RUN pip3 install progress
# RUN pip3 install graphviz

# Setting up User on Image
# Match UID to be same as the one on host machine, run command 'id'
# RUN useradd -u 3333454 -m aberg
# RUN chown -R aberg:aberg nnUNet/
# USER aberg

# Git Credentials
# RUN git config --global user.name "abergsneider"
# RUN git config --global user.email "andresbergsneider@gmail.com"
