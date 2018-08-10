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

First download or clone this repository to a folder of your choice.

To clone, you will need to have established SSH certificates with Fortego Gitlab.  You can find those steps here:
[Install SSH Certs](https://docs.gitlab.com/ee/ssh/)

```bash
git clone git@git.fortegodev.com:BADROBOT/iothub.git
```

### Installing on Windows
On a Windows machine, open up a command prompt and navigate to the iothub\installation\windows folder.

Run the following setup file...
```bash
setup.bat
```

Followed by the installation file
```bash
install.bat
```
Which will produce the following output:

```text
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=Uninstalling IoTHub=-=-=-=-
Skipping iothub as it is not installed
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
-=-=-=-=Installing IoTHub again!=-=-=-=-=-
Processing c:\users\fortegoadmin\desktop\iothub-cli
Requirement already satisfied: docopt in c:\users\fortegoadmin\appdata\local\programs\python\python36\lib\site-packages (from iothub==1.0.0) (0.6.2)
Installing collected packages: iothub
 Running setup.py install for iothub: started
   Running setup.py install for iothub: finished with status 'done'
Successfully installed iothub-1.0.0
```

This will install the iothub cli.  Test it by running the following command:

```bash
iothub
```
And it will print out a list of the available commands you can use.

### Installing on Mac

On a MAC, open up a terminal and navigate to the iothub\installation\mac folder

Run the following commands to run the setup script
```bash
./setup.sh
```

This script installs the Azure IoTHub SDK to your system, along with all other necessary files.
It takes ~3 minutes for it to run through everything, so grab some coffee.

Once it's complete, run the installation file
```bash
./install.sh
```

This will install the iothub cli.  Test it by running the following command:

```bash
iothub
```

And it will print out a list of the available commands you can use.

***Note:***  Mac installation is still not 100%.  Currently working through errors that are popping up with the version of boost.
Unsure if this is a fix on Microsoft's end or something we can do.

###Installing on Linux
For Linux operating systems, follow the instructions located at: [azure-iot-sdk-python](https://github.com/Azure/azure-iot-sdk-python/blob/master/doc/python-devbox-setup.md).


### Examples
The following are the commands to interact with iothub, as well as some examples below

```
iothub device receive -C "HostName=<iothubname>.azure-devices.net;DeviceId=<device name>;x509=true" -c new-device.cert.pem -k new-device.key.pem --protocol=MQTT
```

```
iothub device receive -H <iothubname> -i <device name> -K <access-key>
```

```
iothub service send -m "Test 1" -C "HostName=<iothubname>.azure-devices.net;SharedAccessKeyName=<access name>;SharedAccessKey=<access key>" -i <name of device to send message to> --protocol=AMQP
```

### Usage
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

## Built With
[Microsoft Azure](https://portal.azure.com)

[Python Azure SDK](https://github.com/Azure/azure-iot-sdk-python/blob/master/doc/python-devbox-setup.md)

[Python](https://www.python.org/downloads)

[DocOpt](https://docopt.org)

## Versioning
For the versions available, see the [tags on this repository](https://github.com/dustinsummers/iothub/tags).

## Authors
BADROBOT Team Members:

Matt Gorman

Dustin Summers
