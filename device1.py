import time
import json
import os
import random  # Import the random module
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import Mqtt_proto

mqtt_client = Mqtt_proto.mqt()

def assign_Device_id(device_id):
    #device_id=random.randint(0,1)
    # Generate random Device_id
    return device_id

def update_fill_levels_imgs(device_id):
    # Generate random values for fill levels
    s0, s1, s2, s3,s4 = random.randint(0,1), random.randint(0,1), random.randint(10,11), random.randint(0,1),random.randint(90,100)
    
    levels = [s0, s1, s2, s3,s4]
  #bins/{device_id}/filllevels
    topic = f"*"
    print(topic)
    filling_levels = {"timestamp": str(time.time()), "paper": levels[0], "plastic": levels[1], "metal": levels[2], "miscellaneous": levels[3],"glass":levels[4], "device_id": str(device_id), "datainfo": "fil levels"}
    mqtt_client.publish(f"{topic}", json.dumps(filling_levels), 1)
    print("Published: " + json.dumps(filling_levels))

    return 0

def sensor_data(device_id):  
    # Generate random values for sensor data
    arg1, arg2, arg3, arg4, arg5 = random.randint(0, 10), random.randint(20, 30), random.randint(40, 70), random.randint(0, 5), random.randint(5, 15)
    sensor = {"timestamp": str(time.time()), "deviceId":1, "PIR": 1, "temp": arg2, "humidity": arg3, "fire": arg4, "vibration": arg5, "datainfo": "sensor"}
    mqtt_client.publish("*", json.dumps(sensor), 1)
    print("Published: " + json.dumps(sensor))
    return 0
def number_of_items_in_bin(device_id):
    # Generate random values for item counts
    arg1, arg2, arg3, arg4, arg5 = random.randint(10, 20), random.randint(20, 30), random.randint(8, 15), random.randint(20, 40), random.randint(1, 5)
    items_count = {"timestamp": str(time.time()), "device_id": device_id, "glass": arg1, "metal": arg2, "paper": arg3, "plastic": arg4, "miscellaneous": arg5, "datainfo": "itemcounts"}
    mqtt_client.publish("*", json.dumps(items_count), 1)
    #print("Published: " + json.dumps(items_count))
    return 0
while(1):
    device_id = assign_Device_id(1)
    update_fill_levels_imgs(device_id)
    sensor_data(device_id)
    number_of_items_in_bin(device_id)


