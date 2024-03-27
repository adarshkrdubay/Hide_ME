
import os
import time
import sys
import argparse

# Check if the program is run with sudo permissions
if 'SUDO_UID' not in os.environ.keys():
    print("Run this program with sudo.")
    exit()

# Display copyright information
print("""
HHHHHHHHH     HHHHHHHHIIIIIIIIIDDDDDDDDDDDDD     EEEEEEEEEEEEEEEEEEEEEE     MMMMMMMM               MMMMMMMEEEEEEEEEEEEEEEEEEEEEE
H:::::::H     H:::::::I::::::::D::::::::::::DDD  E::::::::::::::::::::E     M:::::::M             M:::::::E::::::::::::::::::::E
H:::::::H     H:::::::I::::::::D:::::::::::::::DDE::::::::::::::::::::E     M::::::::M           M::::::::E::::::::::::::::::::E
HH::::::H     H::::::HII::::::IDDD:::::DDDDD:::::EE::::::EEEEEEEEE::::E     M:::::::::M         M:::::::::EE::::::EEEEEEEEE::::E
  H:::::H     H:::::H   I::::I   D:::::D    D:::::DE:::::E       EEEEEE     M::::::::::M       M::::::::::M E:::::E       EEEEEE
  H:::::H     H:::::H   I::::I   D:::::D     D:::::E:::::E                  M:::::::::::M     M:::::::::::M E:::::E             
  H::::::HHHHH::::::H   I::::I   D:::::D     D:::::E::::::EEEEEEEEEE        M:::::::M::::M   M::::M:::::::M E::::::EEEEEEEEEE   
  H:::::::::::::::::H   I::::I   D:::::D     D:::::E:::::::::::::::E        M::::::M M::::M M::::M M::::::M E:::::::::::::::E   
  H:::::::::::::::::H   I::::I   D:::::D     D:::::E:::::::::::::::E        M::::::M  M::::M::::M  M::::::M E:::::::::::::::E   
  H::::::HHHHH::::::H   I::::I   D:::::D     D:::::E::::::EEEEEEEEEE        M::::::M   M:::::::M   M::::::M E::::::EEEEEEEEEE   
  H:::::H     H:::::H   I::::I   D:::::D     D:::::E:::::E                  M::::::M    M:::::M    M::::::M E:::::E             
  H:::::H     H:::::H   I::::I   D:::::D    D:::::DE:::::E       EEEEEE     M::::::M     MMMMM     M::::::M E:::::E       EEEEEE
HH::::::H     H::::::HII::::::IDDD:::::DDDDD:::::EE::::::EEEEEEEE:::::E     M::::::M               M::::::EE::::::EEEEEEEE:::::E
H:::::::H     H:::::::I::::::::D:::::::::::::::DDE::::::::::::::::::::E     M::::::M               M::::::E::::::::::::::::::::E
H:::::::H     H:::::::I::::::::D::::::::::::DDD  E::::::::::::::::::::E     M::::::M               M::::::E::::::::::::::::::::E
HHHHHHHHH     HHHHHHHHIIIIIIIIIDDDDDDDDDDDDD     EEEEEEEEEEEEEEEEEEEEEE     MMMMMMMM               MMMMMMMEEEEEEEEEEEEEEEEEEEEEE
By @adarshkrdubay
""")

# List network interfaces and their MAC addresses
os.system("ls /sys/class/net/ > .intfear.lis")
intf_list = []
with open(".intfear.lis", "r") as listfile:
    for line in listfile:
        intf_list.append(line.replace("\n", ""))

# Print out available interfaces and their MAC addresses
for interface in intf_list:
    os.system(f"cat /sys/class/net/{interface}/address > .{interface}.mac")
    with open(f".{interface}.mac", "r") as mac_file:
        mac_id = mac_file.read()
        print(f"{interface} : {mac_id}")

# Prompt the user to choose a network interface and provide a new MAC address
interface_name = input("Enter the interface for which you want to change the MAC ID:\n")
if interface_name in intf_list:
    print(f"{interface_name} selected")
    new_mac_id = input(f"Enter the new MAC ID for {interface_name} (Example: 12:34:56:78:90:01):\n")
    if new_mac_id == "":
        print("No MAC ID provided.")
    else:
        print(f"Changing {interface_name} MAC ID to {new_mac_id}.")
        print("Your system will be disconnected from the network during this process.")
        os.system(f"sudo ifconfig {interface_name} down")
        os.system(f"sudo ifconfig {interface_name} hw ether {new_mac_id}")
        os.system(f"sudo ifconfig {interface_name} up")
        print(f"Your MAC ID is changed to {new_mac_id}")
else:
    print("No such interface")

# Define command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--times", "-t", default=30, help="set time for change")
args = parser.parse_args()

# Check if AnonSurf is installed and install it if not
if not os.path.exists('/usr/bin/anonsurf'):
    print("Anonsurf not found")
    print("Installing dependencies")
    if not os.path.exists('/usr/bin/git'):
        print("Git not found")
        os.system("sudo apt install git")
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git")
    os.system("cd kali-anonsurf/")
    os.system("sudo ./installer.sh")
    print("Installation completed. Exit the shell and run the code again.")
    sys.exit()

# Function to start Tor
def start_tor():
    print("Press ctrl+c to stop")
    os.system(f"{opt} anonsurf start")

# Function to periodically change identity (IP address)
def change_identity():
    while True:
        time.sleep(int(args.times))
        os.system(f"{opt} anonsurf changeid")
        os.system(f"{opt} anonsurf myip")

# Determine if the user wants to use GUI or CLI for Tor
options = input("Do you want:\n1) GUI based\n2) CLI\nEnter your option:")
if options == "1":
    opt = ""  # No sudo needed for GUI
    start_tor()
    change_identity()
elif options == "2":
    opt = "sudo "  # sudo needed for CLI
    start_tor()
    change_identity()
else:
    print("Wrong option")

# Revert the MAC address back to the original one if requested
back_to_same = input("Press Enter to change MAC ID back to normal:\n")
if back_to_same == "":
    old_mac_id = open(f".{interface_name}.mac", "r").read()
    print(f"Changing {interface_name} MAC ID to {old_mac_id}")
    print("Your system will be disconnected from the network during this process.")
    os.system(f"sudo ifconfig {interface_name} down")
    os.system(f"sudo ifconfig {interface_name} hw ether {old_mac_id}")
    os.system(f"sudo ifconfig {interface_name} up")
    print(f"Your MAC ID is changed back to {old_mac_id}")
else:
    print("Bye")

exit()
