from pprint import pprint

# Dictionnary representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "Cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1.",
}

#  Simple Print
print("\n_______ Simple Print _______")
print(f"device : {device}")
print(f"device name : {device['name']}")

# Pretty Print
print("\n_______ Pretty Print _______")
pprint(device)

#  For Loop, nicely formatted print
print("\n_______ For Loop _______")
for key,value in device.items():
    print(f"{key:>16s} : {value}")