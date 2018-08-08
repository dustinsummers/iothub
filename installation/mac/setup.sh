#!/usr/bin/env bash
cwd=$(pwd)
printf "\n=-=-=-=-=-=-=-=- Setting up IoTHub Environment -=-=-=-=-=-\n"
printf "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-====-=--=-=-=-=-=-\n"
sudo -H pip uninstall azure_iothub_device_client-1.4.2-py2-none-any.whl
sudo -H pip uninstall azure_iothub_service_client-1.4.2-py2-none-any.whl
sudo -H pip3 uninstall azure_iothub_service_client-1.4.2-py2-none-any.whl
sudo -H pip3 uninstall azure_iothub_device_client-1.4.2-py2-none-any.whl


printf "\n=-=-= Updating brew =-=-=\n"
brew update

printf "\n=-=-= Installing required packages =-=-=\n"
brew install git cmake pkgconfig openssl ossp-uuid curl boost-python3
brew upgrade cmake
brew upgrade boost-python3

printf "\n=-=-= Linking curl =-=-=\n"
brew link curl --force

printf "\n=-=-= Setting Curl Link =-=-=\n"
export DYLD_LIBRARY_PATH="/usr/local/Cellar/curl/*/lib:$DYLD_LIBRARY_PATH"

printf "\n=-=-= Cloning Python Azure IoT SDK =-=-=\n\n"
cd ../..
mkdir SDK
cd SDK
git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git
cd azure-iot-sdk-python

printf "\n\n=-=-= Building C Submodule for xCode =-=-=\n\n"
cd c
mkdir cmake
cd cmake
cmake -DOPENSSL_ROOT_DIR:PATH=/usr/local/opt/openssl ..
cmake --build .


printf "\n\n=-=-= Building Python SDK =-=-=\n\n"
cd ../../build_all/mac
printf "\n\n=-=-= Setting up Python SDK =-=-=\n\n"
./setup.sh --python-version 3.6
printf "\n\n=-=-= Building shared object files from Python SDK =-=-=\n\n"
cp $cwd/.release.sh release.sh
./release.sh
printf "\n\n=-=-= Installing Python Packages =-=-=\n\n"
sudo -H pip3 install pem
printf "\n\n=-=-= Installing shared object files =-=-=\n\n"
cd ../../SDK/azure-iot-sdk-python/build_all/mac
printf "\n=-=-= Installing Azure IoTHub Device Client =-=-=\n\n"
sudo -H pip3 install release_device_client/dist/azure_iothub_device_client-1.4.2-py3-none-any.whl
printf "\n=-=-= Installing Azure IoTHub Service Client =-=-=\n\n"
sudo -H pip3 install release_service_client/dist/azure_iothub_service_client-1.4.2-py3-none-any.whl

printf "\n=-=-=Cleaning Up=-=-="
cd ../../../..
rm -rf SDK
ls -al
printf "\n=-=-=Finished=-=-="

