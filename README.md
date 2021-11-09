# IOTHUB

IOTHUB is a Command Line Interface tool written in Python for interacting with Microsoft Azure IoT Hub Services.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Preqrequisites

Ensure you have a version of python installed on your system.
```
python --version or python3 --version
```
If you don't have python, install it here: [python.org](https://www.python.org/downloads/).

Also, you will need information for the various IoT Hub Devices/Service that you will be interacting with.  We are working on getting Fortego Test Devices set up, and test scripts will be written catered to those devices for testing/development/pentesting purposes.

## Installation

To use IoTHub, install [Docker](https://www.docker.com/get-started).

Next, reach out maintainers (dustin@dustn.dev) to be granted permissions to pull the Docker Image.

Once installed, run the following command:

```bash
docker pull dustinsummers/iothub
```

The installation takes ~2 minutes.

Once installed, run the following command:

```bash
docker tag dustinsummers/iothub iothub
docker run iothub
```

This should print out the following:

```bash
iothub
Usage:
    iothub device receive (-C|--connect) <connection-string> [--protocol=<protocol>]
    iothub device receive (-C|--connect) <connection-string> (-c|--certificate) <RSA-cert> (-k|--key) <RSA-key> [--protocol=<protocol>]
    iothub device receive (-H|--host) <host-name> (-i|--id) <device-id> (-K|--access-key) <access-key> [--protocol=<protocol>]
    iothub device receive (-H|--host) <host-name> (-i|--id) <device-id> (-c|--certificate) <RSA-cert> (-k|--key) <RSA-key> [--protocol=<protocol>]
    iothub service send (-m|--message) <message> (-C|--connect) <connection-string> (-i|--id) <device-id> [--protocol=<protocol>]
    iothub service send (-m|--message) <message> (-H|--host) <host-name> (-N|--access-name) <access-name> (-K|--access-key) <access-key> (-i|--id) <device-id> [--protocol=<protocol>]

```

### Examples
The following are the commands to interact with iothub, as well as some examples below

Note: In order to reference files on your host machine inside of the Docker container, you must add the following to the command:

```bash
docker run -v /path/to/your/files:/mnt/path iothub
```

```bash
docker run -v /path/to/certs:/mnt/certs iothub device receive -C "HostName=<iothubname>.azure-devices.net;DeviceId=<device name>;x509=true" -c /mnt/certs/new-device.cert.pem -k /mnt/certs/new-device.key.pem --protocol=MQTT
```

```bash
docker run iothub device receive -H <iothubname> -i <device name> -K <access-key>
```

```bash
docker run iothub service send -m "Test 1" -C "HostName=<iothubname>.azure-devices.net;SharedAccessKeyName=<access name>;SharedAccessKey=<access key>" -i <name of device to send message to> --protocol=AMQP
```

### Usage
```bash

iothub device receive (-C|--connect) <connection-string> [--protocol=<protocol>]

iothub device receive (-C|--connect) <connection-string> (-c|--certificate) <RSA-cert> (-k|--key) <RSA-key> [--protocol=<protocol>]

iothub device receive (-H|--host) <host-name> (-i|--id) <device-id> (-K|--access-key) <access-key> [--protocol=<protocol>]

iothub device receive (-H|--host) <host-name> (-i|--id) <device-id> (-c|--certificate) <RSA-cert> (-k|--key) <RSA-key> [--protocol=<protocol>]

iothub service send (-m|--message) <message> (-C|--connect) <connection-string> (-i|--id) <device-id> [--protocol=<protocol>]

iothub service send (-m|--message) <message> (-H|--host) <host-name> (-N|--access-name) <access-name> (-K|--access-key) <access-key> (-i|--id) <device-id> [--protocol=<protocol>]

Options:

-C,              --connect                   Entire connection string (see example below for sample connection string)

-H,              --host                      Hostname for configuration of ConnectionString

-N,              --access-name               Shared Access Key Name for configuration of connection String

-K,              --access-key                Shared Access Key for configuration of Connection String

-i,              --id                        Device ID for configuration of Connection String

-h,              --help                      Show this screen.

-V,              --version                   Show version.

-c,              --certificate               RSA Certificate Provided for access to device

-k,              --key                       RSA Private Key Provided for access to device

-m,              --message                   Message to send to device

--protocol=<protocol>                        Protocol to use. Can be HTTP, AMQP, AMQP_WS, MQTT, MQTT_WS. [default: AMQP]
```

## Built With
[Microsoft Azure](https://portal.azure.com)

[Python Azure SDK](https://github.com/Azure/azure-iot-sdk-python/blob/master/doc/python-devbox-setup.md)

[Python](https://www.python.org/downloads)

[Docker](https://www.docker.com)

[DocOpt](https://docopt.org)

## Versioning
For the versions available, see the [tags on this repository](https://github.com/dustinsummers/iothub/tags).

## Authors
Dustin Summers
