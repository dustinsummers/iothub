#!/usr/bin/env bash
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA Tests =-=-=-=-\n"
iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem

printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running Connection String Tests =-=-=-=-\n"
iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=g/yFqDtb//4rMTKKkr2UL3Oq0XBCaFRaH1uFam5778k="

printf "\n=-=-=-=- End Tests =-=-=-=-=-\n"