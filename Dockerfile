## Image to base ours on
FROM debian

## Environment variables to configure things
## Setting shell so pipenv shell works
ENV SHELL=/bin/bash

## Update and install dependencies
RUN apt update && \
  apt upgrade -y && \
  apt install python3-pip -y && \
  pip3 install pandas && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-soycode