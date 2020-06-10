#Configure Packet Forwarder Program
#Configures the packet forwarder based on the YAML File and Env Variables
import os
import subprocess
import yaml
import json
from pprint import pprint

from time import sleep
moduleId = int(os.environ['LORAMODULE'])
#moduleId = 0

print("Sleeping 10 seconds")
sleep(10)

#Configuration function

def genConfig(loraFile, config, configLora):

    with open(loraFile) as jsonFile:
        newConfig = json.load(jsonFile)

    #Fill out the JSON File from the YAML File
    newConfig['gateway_conf']['contact_email'] = config['user']['email-address']
    newConfig['gateway_conf']['description'] = config['gateway-info']['gateway-description']
    newConfig['gateway_conf']['gateway_ID'] = configLora['packet-forwarder-eui']

    newConfig['gateway_conf']['ref_altitude'] = config['location']['alt']
    newConfig['gateway_conf']['ref_latitude'] = config['location']['lat']
    newConfig['gateway_conf']['ref_longitude'] = config['location']['lon']


    newConfig['gateway_conf']['servers'][0]['server_address'] = configLora['router']
    #if ttn
    if(configLora['providerType'] == "TTN"):
        newConfig['gateway_conf']['servers'][0]['serv_type'] = "ttn"
        newConfig['gateway_conf']['servers'][0]['serv_gw_key'] = configLora['packet-forwarder-key']
        newConfig['gateway_conf']['servers'][0]['serv_gw_id'] = configLora['packet-forwarder-id']
        newConfig['gateway_conf']['servers'][0]['serv_port_up'] = 1700
        newConfig['gateway_conf']['servers'][0]['serv_port_down'] = 1700

    #If Loriot
    elif(configLora['providerType'] == "LORIOT"):
        newConfig['gateway_conf']['servers'][0]['serv_type'] = "semtech"
        newConfig['gateway_conf']['servers'][0]['serv_port_up'] = 1700
        newConfig['gateway_conf']['servers'][0]['serv_port_down'] = 1700

    else:
        newConfig['gateway_conf']['servers'][0]['serv_type'] = "semtech"
        newConfig['gateway_conf']['servers'][0]['serv_port_up'] = 1700
        newConfig['gateway_conf']['servers'][0]['serv_port_down'] = 1700

    #GPS Module
    if(config['gps']['enabled'] == True):
        newConfig['gateway_conf']['gps'] = True;
        newConfig['gateway_conf']['fake_gps'] = False;

    else:
        newConfig['gateway_conf']['gps'] = True;
        newConfig['gateway_conf']['fake_gps'] = False;

    #pprint(newConfig)

    with open(loraFile, 'w') as jsonOut:
        json.dump(newConfig, jsonOut)





with open("/opt/iotloragateway/config/gateway_configuration.yml", 'r') as yamlFile:
    try:
        config = yaml.safe_load(yamlFile)
        configLora1 = config['packet-forwarder-1']
        configLora2 = config['packet-forwarder-2']
    except yaml.YAMLError as exc:
        print(exc)
#Write configuration file for HAT packet
genConfig('local_conf_HAT.json', config, configLora1)

#Write configuration file for SG0
genConfig('local_conf_sg0.json', config, configLora1)

#Write configuration file for SG1
genConfig('local_conf_sg1.json', config, configLora2)




#If HAT Enabled


#Reset on pin 38
while True:
    if(moduleId == 0):
        if(configLora['enabled'] == False):
            print("Forwarder Disabled")
            while True:
                sleep(120)
        else:
            sleep(10)
            print("Nebra Smart Gateway 1")
            print("Starting")
            os.system("./reset-38.sh")
            sleep(2)
            os.system("./packetforwarder_sg0")
            print("Software crashed, restarting, hatsg1")
    elif(moduleId == 1):
        if(configLora['enabled'] == False):
            print("Forwarder Disabled")
            while True:
                sleep(120)
        else:
            sleep(10)
            print("Nebra Smart Gateway 2")
            print("Starting")
            os.system("./reset-39.sh")
            sleep(2)
            os.system("./packetforwarder_sg2")
            print("Software crashed, restarting, sg1")



#If SG1 Enabled
#Start Packet Forwarder SG1
#Reset on pin 39
#print("Nebra Smart Gateway")
#print("Resetting concentrator pin 39")

#sleep(10)
#print("Starting")
#subprocess.Popen("./packetforwarder_sg1")


#Sleep forever
