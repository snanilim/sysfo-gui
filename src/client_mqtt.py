import paho.mqtt.client as mqtt
import uuid, json, os
import datetime
from hepler import *


class MQTTClient(object):
    def __init__(self, *args, **kwargs):
        try:
            uuid.uuid4
            r = str(uuid.uuid4())
            
            self.result = bool
            self.msg = dict
            self.device_uid = str

            self.BROKER_IP = "broker.hivemq.com"
            self.PORT = 1883

            self.client = mqtt.Client(r)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.BROKER_IP, self.PORT, 60)

            print(f"Connected to {0}, starting MQTT loop")
            # self.client.loop_forever()
            # self.client.loop_start()
        except Exception as e:
            print("error", e)

    def on_message(self,client,userdata,message):
        print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
        msg = str(message.payload.decode("utf-8"))

        msg_data = json.loads(msg)
        auth_value = msg_data.get("auth", "")

        data = has_data_on_file()

        if data:
            print('msg', msg)
        elif 'auth' in msg_data and auth_value == 1:
            self.msg = msg_data
            # value = msg_data.get("result", "")
            # device_uid = msg_data.get("device_uid", "")
            # time_frame = msg_data.get("time_frame", "")
            # self.result = eval(value)
            # self.device_uid = device_uid
            # self.time_frame = time_frame
            self.on_loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("srdl/res_login/", 1)

    def on_subscribe(self, topicUri):
        self.client.subscribe(topicUri, 1)

    def on_publish(self, topicUri, message):
        topic = message
        topic_dump = json.dumps(topic)
        self.client.publish(topicUri, topic_dump)
        print('Publish')

    def on_loop_forever(self):
        print('work')
        self.client.loop_forever()

    def on_loop_stop(self):
        print('work')
        self.client.loop_stop()
        self.client.disconnect()
