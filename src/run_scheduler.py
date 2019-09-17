from get_data import *
from datetime import datetime
import sched, time, ast
s = sched.scheduler(time.time, time.sleep)

def write_info():
    print('write_info')


def get_info(sc): 
    data = {
        "info": 1,
        "status": 1,
        "idle": 0, # need do be done later
        "cpu": 1,
        "memory": 1,
        "disk": 1,
        "process": 0,
        "network": 1
    }

    res_info = getData(data)
    # print('res_info', res_info)

    fileRead = open("./idlefile.txt", "r")
    data = fileRead.read()
    data = ast.literal_eval(data)
    clickCount = data['click']
    pressCount = data['press']

    count = {
        'mouse_click_count' : clickCount,
        'keyboard_press_count' : pressCount
    }
    res_info.update({'count': count})



    time = datetime.strptime(format(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
    year = str(time.year)
    month = str(time.month)
    day = str(time.day)
    hour = str(time.hour)
    hour = str(time.hour)
    minuteNumber = str(time.minute)
    date_time = year + "-" + month + "-" + day + "-" + hour + "-" + minuteNumber
    
    f = open(f"./file-{date_time}.txt", "w")
    f.write(str(res_info))
    f.close()



    fileWrite = open("./idlefile.txt", "w")
    message = {
        "click": 0,
        "press": 0
    }
    fileWrite.write(str(message))
    fileWrite.close()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(res_info)

    s.enter(1, 1, get_info, (sc,))


def run_schedule():
    s.enter(1, 1, get_info, (s,))
    s.run()

if __name__ == "__main__":
    run_schedule()
