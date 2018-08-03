#!/usr/bin/env bash
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n=-=-=-=-=Uninstalling IoTHub=-=-=-=-\n"
pip3 uninstall iothub -y
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n-=-=-=-=Installing IoTHub again!=-=-=-=-=-\n"
pip3 install .
