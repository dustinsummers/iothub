#!/usr/bin/env bash
cwd=$(pwd)
printf "\n=-=-=-=-=-=-=-=- Setting up IoTHub Environment -=-=-=-=-=-\n"
printf "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-====-=--=-=-=-=-=-\n"
printf "\n=-=-=-=-=-=-=-=- Ensuring we have the latest Python 3 =-=-=-=-=-=\n"
sudo -H pip3 uninstall azure_iothub_service_client-1.4.2-py3-none-manylinux1_x86_64.whl -y
sudo -H pip3 uninstall azure_iothub_device_client-1.4.2-py3-none-manylinux1_x86_64.whl -y


printf "\n=-=-= Updating APT-GET =-=-=\n"
sudo apt-get update

printf "\n=-=-= Installing required packages =-=-=\n"
sudo apt-get install -y git cmake build-essential curl libcurl4-openssl-dev libssl-dev uuid-dev

printf "\n=-=-= Cloning Python Azure IoT SDK =-=-=\n\n"
cd ../..
mkdir SDK
cd SDK
git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git
cd azure-iot-sdk-python

printf "\n\n=-=-= Building C Submodule from CMake =-=-=\n\n"
cd c
mkdir cmake
cd cmake
cmake -DOPENSSL_ROOT_DIR:PATH=/usr/local/opt/openssl ..
cmake --build .

printf "\n\n=-=-= Building Python SDK =-=-=\n\n"
cd ../../build_all/linux

printf "\n\n=-=-= Setting up Python SDK =-=-=\n\n"
./setup.sh --python-version 3.6

printf "\n\n=-=-= Building shared object files from Python SDK =-=-=\n\n"
./release.sh --build-python 3.6

printf "\n\n=-=-= Installing Python Packages =-=-=\n\n"
sudo -H pip3 install pem

printf "\n\n=-=-= Installing shared object files =-=-=\n\n"
printf "\n=-=-= Installing Azure IoTHub Device Client =-=-=\n\n"
sudo -H pip3 install release_device_client/dist/azure_iothub_device_client-1.4.2-py3-none-manylinux1_x86_64.whl

printf "\n=-=-= Installing Azure IoTHub Service Client =-=-=\n\n"
sudo -H pip3 install release_service_client/dist/azure_iothub_service_client-1.4.2-py3-none-manylinux1_x86_64.whl

printf "\n=-=-=Cleaning Up=-=-="
cd ../../../..
rm -rf SDK
ls -al
printf "\n=-=-=Finished=-=-="

