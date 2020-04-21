FROM python:latest

ENV WORKDIR=/project
WORKDIR $WORKDIR

EXPOSE 8888 8888
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update; \
    apt-get upgrade; \
    apt-get dist-upgrade;
    apt-get install -y python3 python3-pip pandoc texlive-xetex

RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime; \
    dpkg-reconfigure --frontend noninteractive tzdata


CMD pip3 install -r requirements.txt; \
    jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root