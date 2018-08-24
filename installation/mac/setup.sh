#!/usr/bin/env bash
echo "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
echo "\n=-=-=-=-= Uninstalling previous version of the SDK =-=-=-=\n"
brew update
brew install boost-python3
sudo -H pip3 uninstall azure_iothub_device_client -y
sudo -H pip3 uninstall azure_iothub_service_client -y

echo "\n=-=-=-=-= Installing Azure SDK's for IoTHub =-=-=-=-\n"
sudo -H pip3 install azure_iothub_device_client
sudo -H pip3 install azure_iothub_service_client
sudo -H pip3 install pem
sudo -H pip3 install docopt
echo "\n=-=-=-=-= Finished =-=-=-=-\n"
