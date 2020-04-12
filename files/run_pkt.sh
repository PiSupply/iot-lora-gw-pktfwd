#!/usr/bin/env bash

#Run Packetforward
#This script runs on the boot of the container

#python3 -u configurePktFwd.py

#Lets see if we can bodge
./reset-38.sh
./reset-39.sh
./packetforwarder_sg0 && ./packetforwarder_sg1
