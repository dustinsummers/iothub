FROM ubuntu:16.04
MAINTAINER Dustin Summers <dustin.summers@fortegollc.com
ENV boost="http://archive.ubuntu.com/ubuntu/pool/universe/b/boost1.58/libboost1.58-all-dev_1.58.0+dfsg-5ubuntu3.1_amd64.deb"

# update source list for apt-get
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe" | tee -a /etc/apt/sources.list
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates main universe" | tee -a /etc/apt/sources.list
#RUN cat /etc/apt/sources.list

# install system-wide deps for python
RUN apt-get -yqq update
RUN apt-get -yqq install wget python-pip python3 curl build-essential libcurl4-openssl-dev libssl-dev uuid-dev
RUN apt-get -yqq install libboost-all-dev
#RUN apt-get install --allow-downgrades libboost1.58-dev


# pull in all code to docker and set working directory
COPY . /app
WORKDIR /app

# install boost dependency
#RUN mkdir dependencies
#ORKDIR /app/dependencies
#RUN wget --content-disposition $boost
#RUN pwd
#RUN ls

#RUN apt install .

# install iothub
#RUN cd /app && apt install libboost1.58-all-dev.deb
#WORKDIR /app
RUN pip install --upgrade pip
RUN pip install pem
RUN pip install azure-iothub-device-client
RUN pip install azure-iothub-service-client
RUN pip install .
RUN python --version
RUN python3 --version

 # fetch app specific deps
#RUN pip install pem
#RUN pip install docopt
#RUN pip install azure-iothub-device-client
#RUN pip install azure-iothub-service-client

#Entry point for app
ENTRYPOINT ["iothub"]
