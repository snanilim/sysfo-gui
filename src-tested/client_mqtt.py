import paho.mqtt.client as mqtt
import uuid, json, os, ast
import datetime
from helper import *
from get_data import *


class MQTTClient(object):
    def __init__(self, *args, **kwargs):
        print('args', args[0])
        print('args', kwargs)
        try:
            self.dirPath = str
            uuid.uuid4
            r = str(uuid.uuid4())
            
            self.result = bool
            self.msg = dict
            self.device_uuid = str

            self.BROKER_IP = "broker.hivemq.com"
            self.PORT = 1883

            self.client = mqtt.Client(r)
            offline = {
                "status": "offline"
            }
            
            conf_data = has_data_on_file(args[0])
            if conf_data:
                token_obj = get_dec_data(conf_data)
                token_obj = token_obj.replace("'", "\"")
                token_obj = eval(token_obj)
                device_uuid = token_obj['device_uuid']

                offline_dump = json.dumps(offline)
                self.client.will_set(f"srdl/res_offline/{device_uuid}/", payload = offline_dump, qos=1, retain=False)
            
            
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.BROKER_IP, self.PORT, 60)

            print(f"Connected to {0}, starting MQTT loop")
            # self.client.loop_forever()
            # self.client.loop_start()
        except Exception as e:
            print("error", e)
            

    def on_message(self,client,userdata,message):
        try:
            print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
            msg = str(message.payload.decode("utf-8"))
            
            msg_data = json.loads(msg)
            
            auth_value = msg_data.get("auth", "")
            info_value = msg_data.get("info", "")
            

            conf_data = has_data_on_file(self.dirPath)
            
            if conf_data:
                token_obj = get_dec_data(conf_data)
                token_obj = token_obj.replace("'", "\"")
                token_obj = eval(token_obj)
                device_uuid = token_obj['device_uuid']

                if 'info' in msg_data and info_value == 1:
                    self.get_and_send_data(msg_data, device_uuid)
                elif 'idle' in msg_data:
                    self.send_idle_status(device_uuid)
            elif 'auth' in msg_data and auth_value == 1:
                print('msg data', msg_data)
                self.msg = msg_data
                self.on_loop_stop()

        except Exception as error:
            print('error', error)


    def on_connect(self, client, userdata, flags, rc):
        try:
            print("Connected with result code " + str(rc))
            # self.client.subscribe("srdl/req_info/", 1)
            conf_data = has_data_on_file(self.dirPath)
            if conf_data:
                token_obj = get_dec_data(conf_data)
                token_obj = token_obj.replace("'", "\"")
                token_obj = eval(token_obj)
                device_uuid = token_obj['device_uuid']
                lab_id = token_obj['lab_id']
                print('token_obj', device_uuid)
                self.client.subscribe(f"srdl/req_info/{device_uuid}/", 1)
                self.client.subscribe(f"srdl/req_idle_status/{device_uuid}/", 1)

                self.client.subscribe(f"srdl/req_info/{lab_id}/", 1)
                self.client.subscribe(f"srdl/req_idle_status/{lab_id}/", 1)

                # self.client.subscribe("srdl/req_info/", 1)
                self.client.subscribe("srdl/req_idle_status/", 1)

                self.init_start_info(device_uuid)
        except Exception as error:
            print('error', error)


    def on_subscribe(self, topicUri):
        self.client.subscribe(topicUri, 1)

    def on_publish(self, topicUri, message):
        try:
            topic = message
            topic_dump = json.dumps(topic)
            self.client.publish(topicUri, topic_dump)
            print('Publish')
        except Exception as error:
            print('error', error)

    def on_loop_forever(self):
        print('work')
        self.client.loop_forever()

    def on_loop_stop(self):
        print('work')
        self.client.loop_stop()
        self.client.disconnect()


    def get_and_send_data(self, msg_data, device_uuid):
        try:
            mypath = f"{self.dirPath}/config/file"
            all_info = []
            for (dirpath, dirnames, filenames) in os.walk(mypath):

                has_more_files = False
                if len(filenames) > 3:
                    filenames = filenames[0:3]
                    has_more_files = True
                all_info.append({"has_more_files": has_more_files})

                for fileName in filenames:
                    fileRead = open(f"{mypath}/{fileName}", "r")
                    data = fileRead.read()
                    data = data.replace("'", "\"")
                    data = eval(data)
                    
                    all_info.append(data)
                    fileRead.close()
                    os.remove(f"{mypath}/{fileName}")
                break
            
            topic = all_info
            topic_dump = json.dumps(topic)
            self.client.publish(f"srdl/res_info/{device_uuid}/", topic_dump)
        except Exception as error:
            print('error', error)

    def send_idle_status(self, device_uuid):
        try:
            all_info = {}

            idle_info = getIdleTime(self.dirPath)
            all_info.update({'idle': idle_info})

            status_info = getStatus()
            all_info.update({'status': status_info})

            topic = all_info
            topic_dump = json.dumps(topic)
            self.client.publish(f"srdl/res_idle_status/{device_uuid}/", topic_dump)
        except Exception as error:
            print('error', error)

    def init_start_info(self, device_uuid):
        try:
            all_info = {}

            status_info = getStatus()
            all_info.update({'status': status_info})

            mac_addr_value = mac_addr()
            all_info.update({'mac_addr': mac_addr_value})

            gateway_ip_value = gateway_ip()
            all_info.update({'gateway_ip': gateway_ip_value})

            get_platform_value = get_platform()
            all_info.update({'platform': get_platform_value})

            user_name_value = user_name()
            all_info.update({'user_name': user_name_value})

            all_info.update({'device_uuid': device_uuid})

            topic = all_info
            topic_dump = json.dumps(topic)
            self.client.publish(f"srdl/start_status/{device_uuid}/", topic_dump)
        except Exception as error:
            print('error', error)
        


