FROM ubuntu:latest
MAINTAINER Dustin Summers <dustin@dustn.dev>
ENV TERM linux

# pull in dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update \
    && apt-get install -yqq software-properties-common \
                            wget \
                            git \
                            cmake \
                            build-essential \
                            uuid-dev \
                            sudo \
                            libssl-dev \
                            libcurl4-openssl-dev \
                            libboost-all-dev \
                            curl \
                            python3-setuptools \
                            python3-pip

# setup sudo option (required for later install purposes)
RUN useradd -m docker \
    && echo "docker:docker" | chpasswd \
    && adduser docker sudo
RUN mkdir /etc/sudoers.d/ubuntu \
    && echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > ubuntu

# Make directory for SDK
RUN mkdir /SDK
WORKDIR /SDK

# clone IoTHub SDK's
RUN git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git

# configure Python
RUN pip3 install --upgrade pip
RUN pip3.6 install pem
RUN pip3 install wheel

# build SDK's
RUN cd azure-iot-sdk-python/c \
    && mkdir cmake \
    && cd cmake \
    && sudo cmake .. \
    && sudo cmake --build .

# setup and build .so files for python 3.6
WORKDIR azure-iot-sdk-python/build_all/linux
RUN ./release.sh --build-python 3.6

# install device and service client packages
RUN pip3.6 install release_device_client/dist/azure_iothub_device_client-1.4.2-py3-none-manylinux1_x86_64.whl
RUN pip3.6 install release_service_client/dist/azure_iothub_service_client-1.4.2-py3-none-manylinux1_x86_64.whl

# rm /SDK directory to free up space
#RUN ls -al
#RUN rm -rf /SDK
#RUN ls -al

# pull in all code to docker and set working directory
COPY . /app
WORKDIR /app

#if only this worked...
##RUN pip3 install azure-iothub-device-client
##RUN pip3 install azure-iothub-service-client

# install iothub
RUN pip3 install .


# entry point for app
ENTRYPOINT ["iothub"]
