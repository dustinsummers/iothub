printf "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n=-=-=-=-=Uninstalling IoTHub=-=-=-=-"
pip3 uninstall iothub -y
printf "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n-=-=-=-=Installing IoTHub again!=-=-=-=-=-"
pip3 install .
