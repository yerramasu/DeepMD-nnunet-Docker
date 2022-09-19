FROM ubuntu:18.04
RUN mkdir /home/input
RUN mkdir /home/output
COPY pipeline.sh /home
RUN chmod +x /home/pipeline.sh

RUN cd /home
WORKDIR /home

ENTRYPOINT ["/home/pipeline.sh"]