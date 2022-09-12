# Parent Image
FROM nvcr.io/nvidia/pytorch:20.10-py3
RUN apt-get clean && apt-get update -y -qq
RUN apt-get install -y curl git build-essential

ENV LATEST_CONDA "4.4.0"
ENV PATH="/root/anaconda2/bin:${PATH}"
RUN mkdir /home/input
RUN mkdir /home/input/models
COPY penet_best.pth.tar /home/input/model 
RUN curl --silent -O https://repo.continuum.io/archive/Anaconda2-$LATEST_CONDA-Linux-x86_64.sh \
    && bash Anaconda2-$LATEST_CONDA-Linux-x86_64.sh -b -p /root/anaconda2
RUN cd /home && \
     git clone https://github.com/deepmd-mvp1/penet.git  && \
     pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113 && \
     pip install --upgrade pip && \
    cd /home/penet && \
    chmod +x test.sh && \
     pip install -r requirements.txt 
     #python test.py
    #source activate ctpe


#RUN cd /home/penet
#RUN conda env create -f environment.yml
#RUN source activate ctpe
#RUN sh test.sh
#RUN pip install keras && conda install pygpu
