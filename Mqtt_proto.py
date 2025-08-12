import json
import time
import os
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#import RPi.GPIO as GPIO
dir = os.path.dirname(os.path.abspath(__file__)) + "/"
# AWS IoT Configuration
endpoint = "a2kanv3iybkjnm-ats.iot.us-east-1.amazonaws.com"
client_id = "iotconsole-8c0c84e9-945b-4856-b6a4-637734cbfb98"

root_ca_path = r"C:\Users\saich\Desktop\Python\AWS_IOT\Cloud\AmazonRootCA1.pem"
private_key_path = r"C:\Users\saich\Desktop\Python\AWS_IOT\Cloud\private.key"
certificate_path = r"C:\Users\saich\Desktop\Python\AWS_IOT\Cloud\certificate.pem.crt"
#Initialize AWS IoT MQTT Client
def mqt():
    mqtt_client = AWSIoTMQTTClient(client_id)
    mqtt_client.configureEndpoint(endpoint, 8883)
    mqtt_client.configureCredentials(root_ca_path, private_key_path, certificate_path)
    mqtt_client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queuing
    mqtt_client.configureDrainingFrequency(2)  # Draining: 2 Hz
    mqtt_client.configureConnectDisconnectTimeout(10)  # 10 seconds
    mqtt_client.configureMQTTOperationTimeout(5)  # 5 seconds
    mqtt_client.connect()
# Attach a custom callback to handle incoming messages

    return mqtt_client

    


