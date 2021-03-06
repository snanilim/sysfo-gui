from get_data import *
from helper import *
from datetime import datetime
import sched, time, ast
import datetime
s = sched.scheduler(time.time, time.sleep)

def write_info():
    print('write_info')


def get_info(sc, dirPath):
    try:
        conf_data = has_data_on_file(dirPath)
        # print('conf_data', conf_data)
        if conf_data:
            # print('why call')
            # get data
            data = {
                "info": 1,
                "status": 1,
                "cpu": 1,
                "memory": 1,
                "disk": 1,
                "process": 1,
                "motherboard": 1,
                "network": 1
            }
            res_info = getData(data)
            idle_time = getIdleTime(dirPath)
            res_info.update({'idle': idle_time})

            # print('idle_time', idle_time)



            # get count and update res_info
            fileRead = open(f"{dirPath}/config/idlefile.txt", "r")
            data = fileRead.read()
            data = ast.literal_eval(data)
            clickCount = data['click']
            pressCount = data['press']

            count = {'mouse_click_count' : clickCount,'keyboard_press_count' : pressCount}
            res_info.update({'count': count})


            # get present time and write res_info with the time
            time = datetime.datetime.strptime(format(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
            now = datetime.datetime.now()
            timestamp = datetime.datetime.timestamp(time)
            res_info.update({'timestamp': timestamp})
            date_time = str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "-" + str(time.hour) + "-" + str(time.minute)
            
            f = open(f"{dirPath}/config/file/file-{date_time}.txt", "w")
            f.write(str(res_info))
            f.close()


            # rewrite idle file with 0
            fileWrite = open(f"{dirPath}/config/idlefile.txt", "w")
            message = {"click": 0, "press": 0}
            fileWrite.write(str(message))
            fileWrite.close()

            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(res_info)

            token_obj = get_dec_data(conf_data)
            token_obj = token_obj.replace("'", "\"")
            token_obj = eval(token_obj)
            time_frame = token_obj['time_frame']
            print('time_frame', time_frame)

            s.enter(time_frame, 1, get_info, (sc, dirPath,))
        else:
            s.enter(10, 1, get_info, (sc, dirPath,))
    except Exception as error:
        print('error', error)


def run_schedule(dirPath):
    s.enter(1, 1, get_info, (s, dirPath,))
    s.run()

if __name__ == "__main__":
    dirPath = os.path.dirname(os.path.abspath(__file__))
    s.enter(1, 1, get_info, (s, dirPath))
    s.run()
