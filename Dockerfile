FROM ubuntu:19.04
MAINTAINER Makina Corpus "contact@makina-corpus.com"

ADD . /opt/apps/convert2pdf

RUN apt-get update && \
    apt-get install -y python3-pip \
    libreoffice \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apt/*
RUN pip3 install --no-cache-dir gunicorn && \
    pip3 install --no-cache-dir -e /opt/apps/convert2pdf/

ADD .docker/run.sh /usr/local/bin/run

EXPOSE 8000

CMD ["/bin/sh", "-e", "/usr/local/bin/run"]
