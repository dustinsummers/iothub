echo "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
echo "\n=-=-=-=-= Uninstalling Previous Versions of IoTHub =-=-=-=-\n"
pip3 uninstall iothub -y
echo "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
echo "\n-=-=-=-= Installing IoTHub =-=-=-=-=-\n"
pip3 install ../..
echo "\n-=-=-=-= Finished -=-=-=-=-=-=-=-=-\n"