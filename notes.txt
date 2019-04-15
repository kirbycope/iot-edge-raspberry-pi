# AZURE CLI
`az login`
  - opens the browser to let the user login to Azure
`az acr login -n iotedgeraspberrypi`
  - sets the docker login to use the Azure container

# Azure on the Pi
`sudo journalctl -u iotedge -f`
  - tailed logs
`iotedge restart edgeAgent && iotedge restart edgeHub`
  - restart iot hub and agent runtimes
`sudo systemctl restart iotedge`
  - restart the iot edge security daemon
  