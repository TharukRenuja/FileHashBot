FROM ubuntu:20.04
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get -y update && apt-get install -y python3 python3-pip git
# RUN apt-get -y upgrade
RUN apt-get -y autoremove && apt-get -y autoclean
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD python3 -m filehashbot
