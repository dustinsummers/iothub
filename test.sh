#!/usr/bin/env bash

#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- CLEAR OUT OLD MESSAGES =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/MQTT Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#python SendCloudToDeviceMessage.py "RSA MQTT Test 1"
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/MQTT_WS Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#python SendCloudToDeviceMessage.py "RSA MQTT_WS Test 1"
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT_WS
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/HTTP Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#python SendCloudToDeviceMessage.py "RSA HTTP Test 1"
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=HTTP
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/AMQP Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#python SendCloudToDeviceMessage.py "RSA AMQP Test 1"
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=AMQP
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/AMQP_WS Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#python SendCloudToDeviceMessage.py "RSA AMQP_WS Test 1"
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=AMQP_WS
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
## printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running Connection String Tests =-=-=-=-\n"
## iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=g/yFqDtb//4rMTKKkr2UL3Oq0XBCaFRaH1uFam5778k="
#
#printf "\n=-=-=-=- End Tests =-=-=-=-=-\n"

iothub hello

printf "\n=-=-=-=- Testing Send Scripts from Service =-=-=-=-=-\n"
iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP
iothub service send -m "Test 1" -H  "ScriptRemoteIoTHub.azure-devices.net;" -N "iothubowner" -K "dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP

