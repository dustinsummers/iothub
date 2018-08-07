#!/usr/bin/env bash

#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- CLEAR OUT OLD MESSAGES =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/MQTT Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/MQTT_WS Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT_WS
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
#printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/HTTP Tests =-=-=-=-\n"
#printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
#iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP
#printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
#printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
#iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=HTTP
#printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
#
printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/AMQP Tests =-=-=-=-\n"
printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP
printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=AMQP
printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"

printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running RSA/AMQP_WS Tests =-=-=-=-\n"
printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i thumbprintDevice --protocol=AMQP
printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=thumbprintDevice;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=AMQP_WS
printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"

printf "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n =-=-=-=- Running Connection String Tests =-=-=-=-\n"
printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i MyPythonDevice --protocol=AMQP
printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=g/yFqDtb//4rMTKKkr2UL3Oq0XBCaFRaH1uFam5778k=" --protocol=AMQP
printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"
printf "\n=-=-=- Sending Message to Device =-=-=-=-\n"
iothub service send -m "Test 1" -C "HostName=ScriptRemoteIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=dzsuwr/ePr7Li1Pn/bux4oYKh96NAaJz6pdipGNE/3o=" -i MyPythonDevice --protocol=AMQP_WS
printf "\n=-=-=-=- Message Sent =-=-=-=-\n"
printf "\n=-=-=-=- Retrieving Message =-=-=-=-\n"
iothub device receive -C "HostName=ScriptRemoteIoTHub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=g/yFqDtb//4rMTKKkr2UL3Oq0XBCaFRaH1uFam5778k=" --protocol=AMQP_WS
printf "\n=-=-=-=- End MessageRetrieval  =-=-=-=-=-\n\n"



printf "\n=-=-=-=- End Tests =-=-=-=-=-\n"

#iothub hello
