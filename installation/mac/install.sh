#!/usr/bin/env bash
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
printf "\n=-=-=-=-=Uninstalling IoTHub=-=-=-=-\n"
sudo -H pip uninstall iothub -y
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
printf "\n-=-=-=-=Installing IoTHub! =-=-=-=-=-\n"
sudo -H pip install ../..
printf "\n=-=-= Finished =-=-=\n"
