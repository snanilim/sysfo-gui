import paho.mqtt.client as mqtt
import uuid, json, os, ast
import datetime
from helper import *


class MQTTClient(object):
    def __init__(self, *args, **kwargs):
        self.dirPath = str
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
        info_value = msg_data.get("info", "")

        conf_data = has_data_on_file(self.dirPath)

        if conf_data:
            if 'info' in msg_data and info_value == 1:
                self.get_and_send_data(msg_data)
        elif 'auth' in msg_data and auth_value == 1:
            self.msg = msg_data
            self.on_loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("srdl/req_info/", 1)
        conf_data = has_data_on_file(self.dirPath)
        if conf_data:
            token_obj = get_dec_data(conf_data)
            token_obj = token_obj.replace("'", "\"")
            token_obj = eval(token_obj)
            device_uuid = token_obj['device_uuid']
            print('token_obj', device_uuid)
            self.client.subscribe(f"srdl/req_info/{device_uuid}/", 1)


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


    def get_and_send_data(self, msg_data):
        print('msg_data', msg_data)
        mypath = f"{self.dirPath}/config/file"
        all_info = []
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            for fileName in filenames:
                print('filename', fileName)
                print('fileRead', f"{mypath}/{fileName}")
                fileRead = open(f"{mypath}/{fileName}", "r")
                
                data = fileRead.read()
                data = ast.literal_eval(data)
                all_info.append(data)
            break
        topic = all_info
        topic_dump = json.dumps(topic)
        self.client.publish("srdl/res_info/76f08fa6-93e0-4314-96ff-f772fd3ed5d1/", topic_dump)
        print('f', all_info)

        
