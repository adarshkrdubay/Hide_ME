# HideME: MAC Changer and AnonSurf Utility

## Introduction
HideME is a Python script that provides a utility to change the MAC address of network interfaces and use AnonSurf for anonymous web browsing. It is specifically designed for Parrot Security OS and Kali Linux.

## Features
- Change the MAC address of network interfaces.
- Utilize AnonSurf for anonymous browsing.
- GUI and CLI options available.
- Automatically change Tor identity after a specified time interval.

## Requirements
- Python 3.x
- AnonSurf (included in Parrot Security OS and Kali Linux)

## Installation
1. Clone this repository:

```
git clone https://github.com/adarshkrdubay/Hide_ME.git
```
2. Navigate to the project directory:
```
cd Hide_ME
```
## Usage
1. Run the script with sudo permissions:
```
sudo python3 Hide_ME.py
```
Follow the on-screen instructions to choose the network interface and provide a new MAC address.
Select either GUI or CLI for using AnonSurf.
Optionally, specify the time interval for automatically changing Tor identity using the --times or -t argument:
```
sudo python3 HideME.py --times 60
```
This command will change the Tor identity every 60 seconds.
The script will automatically start AnonSurf and change the MAC address periodically.

## Note
HideME is designed to work on Parrot Security OS and Kali Linux. It may not be compatible with other Linux distributions.
Ensure you have administrative privileges to run the script.
Use caution while changing network settings, as it may affect network connectivity.

# Credits

HideME is inspired by the work of Adarshkrdubay (https://www.adarshkrdubay.tech).
