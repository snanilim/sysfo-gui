from get_data import *
import sched, time
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
        "process": 1,
        "network": 1
    }
    # res_info = getData(data)
    # # print('res_info', res_info)

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(res_info)
    f = open("./idlefile.txt", "r")
    text = f.read()
    print('read', text)
    s.enter(1, 1, get_info, (sc,))


def run_schedule():
    s.enter(1, 1, get_info, (s,))
    s.run()

if __name__ == "__main__":
    run_schedule()
