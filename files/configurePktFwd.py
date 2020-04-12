#Configure Packet Forwarder Program
#Configures the packet forwarder based on the YAML File and Env Variables
import os
import subprocess
import yaml
import json
from pprint import pprint

from time import sleep
#moduleId = int(os.environ['LORAMODULE'])
#moduleId = 0

print("Sleeping 10 seconds")
sleep(10)

#Write configuration file for HAT packet

#Write configuration file for SG0

#Write configuration file for SG1


#If HAT Enabled

#Start Packet Forwarder HAT
#Reset on pin 38
sleep(2)
print("Pi Supply LoRa HAT")
print("Resetting concentrator pin 22")

#sleep(7)
print("Starting")
os.system("./packetforwarder_hat")
while True:
    sleep(120)


#If SG0 Enabled
#Start Packet Forwarder SG0
#Reset on pin 38
sleep(2)
print("Nebra Smart Gateway")
print("Resetting concentrator pin 38")

#sleep(7)
print("Starting")
subprocess.popen("./packetforwarder_sg0")


#If SG1 Enabled
#Start Packet Forwarder SG1
#Reset on pin 39
print("Nebra Smart Gateway")
print("Resetting concentrator pin 39")

sleep(5)
print("Starting")
os.system("./packetforwarder_sg1")


#Sleep forever
while True:
    sleep(120)
