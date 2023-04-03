FROM ubuntu:22.04

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN sed 's@archive.ubuntu.com@free.nchc.org.tw@' -i /etc/apt/sources.list
RUN apt-get update && apt-get install -y ssh python3.11 python3-pip git build-essential curl

RUN mkdir /etc/bocountry
COPY . /etc/bocountry

WORKDIR /etc/bocountry
RUN pip install -r requirements.txt

WORKDIR /etc/bocountry/python
CMD sleep 10 && flask run --host 0.0.0.0 --port 8000
