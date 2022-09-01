# Parent Image
FROM nvcr.io/nvidia/pytorch:20.11-py3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install -y unzip

ENV nnUNet_raw_data_base "/home/nnUNet/data/nnUNet_raw_data_base"
ENV nnUNet_preprocessed "/home/nnUNet/data/nnUNet_preprocessed"
ENV RESULTS_FOLDER "/home/nnUNet/data/models"
ENV seg_model_url  "https://www.dropbox.com/s/m7es2ojn8h0ybhv/Task055_SegTHOR.zip?dl=0"
ENV output_path  "/home/models/Task055_SegTHOR.zip"
RUN mkdir /home/models
RUN wget  -O /home/models/Task055_SegTHOR.zip https://www.dropbox.com/s/m7es2ojn8h0ybhv/Task055_SegTHOR.zip?dl=0
#-O $output_path $seg_model_url
# RUN mkdir /home/models
# COPY Task055_SegTHOR.zip /home/models
COPY pipeline.sh /home
# Installing nnU-Net
RUN cd /home && \
  mkdir /home/input && \
  mkdir /home/output && \
  git clone https://github.com/MIC-DKFZ/nnUNet.git  && \
  mkdir /home/nnUNet/input && \
#   mkdir /home/models && \
  mkdir /home/nnUNet/output && \
  mkdir /home/nnUNet/data && \
  mkdir /home/nnUNet/data/models && \
  mkdir /home/nnUNet/data/nnUNet_raw_data_base && \
  mkdir /home/nnUNet/data/nnUNet_preprocessed && \
  cd /home/nnUNet && \
  pip install -e . && \
  pip3 install progress && \
  pip3 install graphviz && \
  nnUNet_install_pretrained_model_from_zip /home/models/Task055_SegTHOR.zip  && \
  cd /home
RUN chmod +x /home/pipeline.sh
ENTRYPOINT ["/home/pipeline.sh"]
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
