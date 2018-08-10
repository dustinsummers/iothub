#!/usr/bin/env bash
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
printf "\n=-=-=-=-=Uninstalling IoTHub=-=-=-=-\n"
sudo -H pip3 uninstall iothub -y
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
printf "\n-=-=-=-=Installing IoTHub! =-=-=-=-=-\n"
sudo -H pip3 install ../..
printf "\n=-=-= Finished =-=-=\n"
