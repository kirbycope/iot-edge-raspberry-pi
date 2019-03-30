# iot-edge-raspberry-pi

## Prerequisites
- Hardware
   - Raspberry Pi 3B+
   - 5V 2.5A Micro USB power supply
   - Micro SD Card

## Setup the OS for the Raspberry Pi
1. Download Raspbian Stretch Lite and unzip
    - https://www.raspberrypi.org/downloads/raspbian/
1. Download and installer Balena Etcher
    - https://www.balena.io/etcher/
1. Using Balena, flash the Raspbian image (the file previously unzipped) to the SD card
1. Power on the Pi
    - u: pi
    - P: raspberry
1. (Optional) Run the following command to enable Wi-fi
    - `sudo raspi-config`
    - Select option 2, 'Network Options'
    - Select option 2, 'Wi-fi'
    - Select your country from the list
    - Enter your Wi-fi network's SSID
    - Enter your Wi-fi network's passkey
	  - Select 'Finish'
1. (Optional) [Enable SSH to issue command on the Raspberry Pi from your local machine](https://www.raspberrypi.org/documentation/remote-access/ssh/)
    - Run the following command
        - `sudo raspi-config`
   - Select option 5, 'Interfacing Options'
   - Select option 2, 'SSH'
   - Select 'Yes' to enable
   - Select 'OK'
   - Select 'Finish'
   - Run the following command to display your interface configuration
   - You can use PuTTy to open an SSH connection on Windows.
       - If you have git, chances are you already have PuTTy installed.
1. Run the following command to update the OS
   - `sudo apt update && sudo apt full-upgrade -y`

## [Install the Container Runtime on the Raspberry Pi](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux-arm#install-the-container-runtime)
1. Download and install the moby-engine
	  - `curl -L https://aka.ms/moby-engine-armhf-latest -o moby_engine.deb && sudo dpkg -i ./moby_engine.deb`
1. Download and install the moby-cli
	  - `curl -L https://aka.ms/moby-cli-armhf-latest -o moby_cli.deb && sudo dpkg -i ./moby_cli.deb`
1. Run apt-get fix
	  - `sudo apt-get install -f`

## [Install the IoT Edge Security Daemon](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux-arm#install-the-iot-edge-security-daemon)
1. Download and install the standard libiothsm implementation
	  - `curl -L https://aka.ms/libiothsm-std-linux-armhf-latest -o libiothsm-std.deb && sudo dpkg -i ./libiothsm-std.deb`
1. Download and install the IoT Edge Security Daemon
	  - `curl -L https://aka.ms/iotedged-linux-armhf-latest -o iotedge.deb && sudo dpkg -i ./iotedge.deb`
1. Run apt-get fix
	  - `sudo apt-get install -f`

## [Connect Your Device to an IoT Hub](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux-arm#option-1-manual-provisioning)
Manual provisioning reason: Raspberry Pi devices do not come with TPM by default.
