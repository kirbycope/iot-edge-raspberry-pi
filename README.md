# iot-edge-raspberry-pi

## Prerequisites
- Hardware
   - Raspberry Pi 3B+
   - 5V 2.5A Micro USB power supply
   - Micro SD Card
- Software
   - An [IoT hub](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal) in your Azure subscription
   - A [Container registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal) in your Azure subscription
   - [VS Code](https://code.visualstudio.com/) with the following extensions
      - [Azure Account](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)
      - [Azure IoT Edge](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge)
      - [Azure IoT ToolKit](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)
      - [Docker](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker)
      - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Python](https://www.python.org/downloads/)
      - With [pip](https://pip.pypa.io/en/stable/installing/)
      - And ENV variables [set](https://www.tutorialspoint.com/python/python_environment.htm) for python, pip, and wheels
      - So that [iotedgehubdev](https://github.com/Azure/iotedgehubdev#installing) can be installed 

## Raspberry Pi Setup
Set up Azure IoT Edge on a Raspberry Pi 3.

### [Setup the OS for the Raspberry Pi](https://blog.jongallant.com/2017/11/raspberrypi-setup/)
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

### [Install the Container Runtime on the Raspberry Pi](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux-arm#install-the-container-runtime)
1. Download and install the moby-engine
   - `curl -L https://aka.ms/moby-engine-armhf-latest -o moby_engine.deb && sudo dpkg -i ./moby_engine.deb`
1. Download and install the moby-cli
   - `curl -L https://aka.ms/moby-cli-armhf-latest -o moby_cli.deb && sudo dpkg -i ./moby_cli.deb`
1. Run apt-get fix
   - `sudo apt-get install -f`

### [Install the IoT Edge Security Daemon](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux-arm#install-the-iot-edge-security-daemon)
1. Download and install the standard libiothsm implementation
   - `curl -L https://aka.ms/libiothsm-std-linux-armhf-latest -o libiothsm-std.deb && sudo dpkg -i ./libiothsm-std.deb`
1. Download and install the IoT Edge Security Daemon
   - `curl -L https://aka.ms/iotedged-linux-armhf-latest -o iotedge.deb && sudo dpkg -i ./iotedge.deb`
1. Run apt-get fix
   - `sudo apt-get install -f`

### [Register the Raspberry Pi from Azure Portal](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-register-device-portal)
1. Add a new IoT Edge device and copy the resulting connection string
   - On resource constrained devices, it is highly recommended that you set the OptimizeForPerformance environment variable to false as per instructions in the [troubleshooting guide](https://docs.microsoft.com/en-us/azure/iot-edge/troubleshoot#stability-issues-on-resource-constrained-devices)
   
### [Connect the Raspberry Pi to Your IoT Hub](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux-arm#option-1-manual-provisioning)
Manual provisioning reason: Raspberry Pi devices do not come with TPM by default.
1. Run the following command to edit the configuration file
   - `sudo nano /etc/iotedge/config.yaml`
1. Scroll down to the manual provisioning section and replace `<ADD DEVICE CONNECTION STRING HERE>`
1. Press `[Ctrl]`+`[X]`, then `[Y]`, and then `[Enter]` to Exit and Save
1. Run the following command to restart the daemon
   - `sudo systemctl restart iotedge`
1. Run the following command to verify the stauts of the IoT Edge Daemon
   - `systemctl status iotedge`
   - Press `[Ctrl]`+`[C]` to Close
1. Run the following command to list running modules
   - `sudo iotedge list`

## Simulated Device Setup
Set up Azure IoT Edge on a simulated device (for development and testing). This guide uses [Windows](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-windows-with-linux) but [Linux](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux) is also supported.

### [Enable Containers on Windows](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-linux)
Note: Currently Windows 10 Professional or Enterprise is needed. [Source](https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/quick-start-windows-10#prerequisites)
1. Press `[Windows]` and then type `turn windows features` and then press `[Enter]`
1. Check the box next to `Containers` and then select 'OK'
   - Restart your computer to apply the changes

### [Install a Container Engine for Linux on Windows](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-windows#docker-for-linux-containers)
1. Download and install Docker
   - https://www.docker.com/products/docker-desktop
1. Switch to Linux containers (if set to Windows)
   - https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers

### [Register the Simulated Device from Azure Portal](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-register-device-portal)
1. Add a new IoT Edge device and copy the resulting connection string

### [Install the IoT Edge Security Daemon](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-windows#option-1-install-and-manually-provision)
1. Open PowerShell ISE (as an Administrator)
1. Paste in the following script
   ```powershell
   . {Invoke-WebRequest -useb aka.ms/iotedge-win} | Invoke-Expression; `
   Install-SecurityDaemon -Manual -ContainerOs Linux -DeviceConnectionString '<connection-string>'
   ```
1. Replace the `<connection-string>`
1. Press `[F5]` to Run the script
1. Run the following command to check the status
   - `Get-Service iotedge`
1. Run the following command to list the running modules
   - `iotedge list`
1. Run the following command to list the docker image(s)
   - `docker images`
1. (Reference) To update the device see where the runtime is already installed, see [Update an existing installation](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-install-iot-edge-windows#update-an-existing-installation)

## Solution in VS Code

### Create the Solution
1. Select 'View' > 'Command Palette...' > 'Azure IoT Edge: New IoT Edge Solution'
1. Name your solution
1. Select 'Python' module
   - An [IoT module](https://docs.microsoft.com/en-us/azure/marketplace/iot-edge-module) is code executed on the edge device
   - `./modules/{module-name}/Dockerfile.*` will setup the containers with the necessary libraries
1. Name the Python module
   - SampleModule will be prepopulated and provide sample code to listen to the message queue
1. Replace `localhost:5000` with your Azure Container
   - Example: `iotedgeraspbberypi.azurecr.io/samplemodule`
   - This value is stored in `./modules/{module-name}/module.json`
1. You should be prompted to store your credentials in a .git ignored .env file

### Deploy IoT Edge Solution to Simulated Device
1. Right-click the `deployment.template.json` file and select 'Build IoT Edge Solution'
   - Sign-out of Docker Desktop if you have an authentication error from ubuntu:xenial
1. Right-click the `deployment.template.json` file and select 'Generate IoT Edge Deployment Manifest'
1. Right-click the `./config/deployment.amd64.json` file and select 'Create Deployment for Single Device'
1. Select the registered simulated device from your hub
1. In the Azure IoT Hub Devices extension pane, right-click your simulated device and select 'Start Monitoring D2C Message'
   - This will show the messages being sent from the **D**evice **2** the **C**loud
   - Note: To stop the monitoring, use the 'Azure IoT Hub: Stop monitoring D2C messages' command from the Command Palette

### Deploy IoT Edge Solution to Raspberry Pi
1. Select 'arm32v7' as the default platform
1. Right-click the `deployment.template.json` file and select 'Build IoT Edge Solution'
1. Right-click the `deployment.template.json` file and select 'Generate IoT Edge Deployment Manifest'
1. Right-click the `./config/deployment.arm32v7.json` file and select 'Create Deployment for Single Device'
1. Select the registered raspberry pi from your hub
1. In the Azure IoT Hub Devices extension pane, right-click your simulated device and select 'Start Monitoring D2C Message'
   - This will show the messages being sent from the **D**evice **2** the **C**loud
   - Note: To stop the monitoring, use the 'Azure IoT Hub: Stop monitoring D2C messages' command from the Command Palette
