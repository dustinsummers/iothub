#!/usr/bin/env bash
cwd=$(pwd)
printf "\n=-=-=-=-=-=-=-=- Setting up IoTHub Environment -=-=-=-=-=-\n"
printf "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-====-=--=-=-=-=-=-\n"
printf "\n=-=-=-=-=-=-=-=- Ensuring we have the latest Python 3 =-=-=-=-=-=\n"
brew install python3
conda install python=3.7
brew upgrade python3
sudo -H pip3 uninstall azure_iothub_service_client-1.4.2-py3-none-any.whl -y
sudo -H pip3 uninstall azure_iothub_device_client-1.4.2-py3-none-any.whl -y


printf "\n=-=-= Updating brew =-=-=\n"
brew update

printf "\n=-=-= Installing required packages =-=-=\n"
# Original Brew Install: brew install git cmake pkgconfig openssl ossp-uuid curl boost-python3
brew install git cmake pkgconfig ossp-uuid curl
brew upgrade cmake python
xcode-select --install
#brew upgrade boost-python3

printf "\n=-=-= Linking curl =-=-=\n"
brew unlink curl
brew link --force curl

printf "\n=-=-= Setting Curl Link =-=-=\n"
export DYLD_LIBRARY_PATH="/usr/local/Cellar/curl/*/lib:$DYLD_LIBRARY_PATH"

printf "\n=-=-= Cloning Python Azure IoT SDK =-=-=\n\n"
cd ../..
mkdir SDK
cd SDK
git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git
cd azure-iot-sdk-python

printf "\n\n=-=-= Building C Submodule for xCode =-=-=\n\n"
#cd c
#mkdir cmake
#cd cmake
#cmake -G Xcode ..
cd c
mkdir cmake
cd cmake
cmake -DOPENSSL_ROOT_DIR:PATH=/usr/local/opt/openssl ..
cmake --build .

printf "\n\n=-=-= Building Python SDK =-=-=\n\n"
cd ../../build_all/mac
printf "\n\n=-=-= Setting up Python SDK =-=-=\n\n"
cp $cwd/.iot_setup.sh setup.sh
old_setup.sh --python-version 3.7

printf "\n\n=-=-= Building shared object files from Python SDK =-=-=\n\n"
cp $cwd/.iot_release.sh release.sh
./release.sh

printf "\n\n=-=-= Installing Python Packages =-=-=\n\n"
sudo -H pip3 install pem
printf "\n\n=-=-= Installing shared object files =-=-=\n\n"
printf "\n=-=-= Installing Azure IoTHub Device Client =-=-=\n\n"
sudo -H pip3 install release_device_client/dist/azure_iothub_device_client-1.4.2-py3-none-any.whl
printf "\n=-=-= Installing Azure IoTHub Service Client =-=-=\n\n"
sudo -H pip3 install release_service_client/dist/azure_iothub_service_client-1.4.2-py3-none-any.whl

printf "\n=-=-=Cleaning Up=-=-="
cd ../../../..
rm -rf SDK
ls -al
printf "\n=-=-=Finished=-=-="

