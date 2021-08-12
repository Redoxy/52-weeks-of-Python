from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from  pprint import pprint

# empty list for holding devices
devices = list()

# add comment

# for loop to create large number of devices
for index in range(1,101):
    # create device dictionary
    device = dict()

    #  random device name
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # random vendor from choice  of Cisco, Juniper, Arista
    device["vendor"] = choice(["Cisco", "Juniper", "Arista"])
    if device["vendor"] == "Cisco":
        device["os"] =  choice(["ios" , "iosxe", "iosxr", "nxos"])
        device["version"] =  choice(["12.1(T)", "7.0.3.9", "14.07X", "20.45"])
    elif device["vendor"] == "Juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif device["vendor"] == "Arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "3.38"])
    
    # assign IP Address
    device["ip"] = "10.0.0." + str(index)

    print()
    for key,value in device.items():
        print(f"{key:>16s} : {value}")

    # add the device to the list of devices
    devices.append(device)



# use pprint to print data as-is
print("\n_______ Pretty Print _______")
pprint(devices)

# use 'tabulate' to print table of devices
print("\n_______ Sorted devices in tabular format _______")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")),headers="keys"))