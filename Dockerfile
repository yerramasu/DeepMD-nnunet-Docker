# Parent Image
FROM nvcr.io/nvidia/pytorch:20.11-py3

ENV nnUNet_raw_data_base "/home/nnUNet/data/nnUNet_raw_data_base"
ENV nnUNet_preprocessed "/home/nnUNet/data/nnUNet_preprocessed"
ENV RESULTS_FOLDER "/home/nnUNet/data/models"

COPY pipeline.sh /home
# Installing nnU-Net
RUN cd /home && \
  git clone https://github.com/MIC-DKFZ/nnUNet.git  && \
  mkdir /home/nnUNet/input && \
  mkdir /home/nnUNet/output && \
  mkdir /home/nnUNet/data && \
  mkdir /home/nnUNet/data/models && \
  mkdir /home/nnUNet/data/nnUNet_raw_data_base && \
  mkdir /home/nnUNet/data/nnUNet_preprocessed && \
  cd /home/nnUNet && \
  pip install -e . && \
  nnUNet_download_pretrained_model Task009_Spleen && \
  cd /home
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
