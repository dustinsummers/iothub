FROM ubuntu:16.04
MAINTAINER Dustin Summers <dustin.summers@fortegollc.com>

# pull in image dependencies
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y software-properties-common
RUN apt-get -yqq install wget git cmake curl build-essential libcurl4-openssl-dev libssl-dev uuid-dev
RUN curl -V

# clone in SDK's to build manually
RUN mkdir /SDK
WORKDIR /SDK
RUN git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git

# build c module for the SDK
RUN cd azure-iot-sdk-python/c \
    && mkdir cmake \
    && cd cmake \
    && cmake .. \
    && cmake --build . 





# pull in python 3.6
#RUN add-apt-repository ppa:jonathonf/python-3.6
#RUN apt update
#RUN apt -y install python3.6
#RUN apt -y install python3.6-dev
#RUN apt -y install python3.6-dev
#RUN apt -y install python3.6-venv
#RUN wget https://bootstrap.pypa.io/get-pip.py
#RUN python3.6 get-pip.py
#RUN rm /usr/local/bin/pip3
#RUN ln -s /usr/bin/python3.6 /usr/local/bin/python3
#RUN ln -s /usr/local/bin/pip /usr/local/bin/pip3
#RUN apt-get -yqq install libboost-all-dev
#
## pull in all code to docker and set working directory
#COPY . /app
#WORKDIR /app
#
## install iothub
#RUN pip3 install --upgrade pip
#RUN ls /usr/local/lib
#RUN apt-get -y remove 'python3.5'
#RUN pip3.6 install pem
#RUN pip3.6 install azure-iothub-device-client
#RUN pip3.6 install azure-iothub-service-client
#RUN pip3.6 install .
#RUN python --version
#RUN python3 --version
#RUN ls /usr/local/lib

# entry point for app
ENTRYPOINT ["iothub"]