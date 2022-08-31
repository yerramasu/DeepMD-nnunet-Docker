# Parent Image
FROM nvcr.io/nvidia/pytorch:20.11-py3



# Installing nnU-Net
RUN git clone https://github.com/abergsneider/nnUNet.git
WORKDIR /workspace/nnUNet
RUN pip install -e .

# Environment Variables:
ENV nnUNet_raw_data_base "/workspace/nnUNet/nnUNet_data/nnUNet_raw_data_base"
ENV nnUNet_preprocessed "/workspace/nnUNet/nnUNet_data/nnUNet_preprocessed"
ENV RESULTS_FOLDER "/workspace/nnUNet/nnUNet_data/nnUNet_trained_models"

# Installing additional libraries
WORKDIR /workspace/
RUN pip3 install --upgrade git+https://github.com/nanohanno/hiddenlayer.git@bugfix/get_trace_graph#egg=hiddenlayer
RUN pip3 install progress
RUN pip3 install graphviz

# Setting up User on Image
# Match UID to be same as the one on host machine, run command 'id'
# RUN useradd -u 3333454 -m aberg
# RUN chown -R aberg:aberg nnUNet/
# USER aberg

# Git Credentials
# RUN git config --global user.name "abergsneider"
# RUN git config --global user.email "andresbergsneider@gmail.com"
