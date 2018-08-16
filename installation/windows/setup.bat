echo "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
echo "\n=-=-=-=-= Uninstalling previous version of the SDK =-=-=-=\n"
pip3 uninstall azure-iothub-device-client
pip3 uninstall azure-iothub-service-client

echo "\n=-=-=-=-= Installing Azure SDK's for IoTHub =-=-=-=-\n"
pip3 install azure-iothub-device-client
pip3 install azure-iothub-service-client
sudo pip install pem
echo "\n=-=-=-=-= Finished =-=-=-=-\n"
