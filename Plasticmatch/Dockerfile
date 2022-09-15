# Parent Image
FROM nvcr.io/nvidia/pytorch:20.10-py3

RUN  apt-get update && apt-get upgrade -y
RUN  apt-get install -y wget
RUN  apt-get install -y unzip
RUN  apt install -y plastimatch
RUN  apt install -y subversion
RUN cd /home

RUN wget https://github.com/QIICR/dcmqi/releases/download/v1.2.4/dcmqi-1.2.4-linux.tar.gz
RUN cd /home
RUN tar zxvf dcmqi-1.2.4-linux.tar.gz
RUN cp dcmqi-1.2.4-linux/bin/* /usr/local/bin/
# RUN pip install nnunet
RUN pip install pydicom

COPY pipeline.sh /home


# Installing nnU-Net
RUN cd /home 
 
RUN chmod +x /home/pipeline.sh
WORKDIR /home

ENTRYPOINT ["/home/pipeline.sh"]
