from multiprocessing import Pool, freeze_support
from time import sleep
import os, ast, json, platform
import datetime
from helper import *

# all your methods declarations above go here
# (...)

ovalue = 0

def loginProcess(largefile):
    try:
        dirPath = os.path.dirname(os.path.abspath(__file__))
        data = has_data_on_file(dirPath)
        if data:
            token_obj = get_dec_data(data)
            token_obj = token_obj.replace("'", "\"")
            token_obj = eval(token_obj)
            token_value = token_obj['auth_token']

            if token_value:
                print('hello')
                from client_mqtt import MQTTClient
                client = MQTTClient(dirPath)
                client.dirPath = dirPath
                client.on_loop_forever()
            else:
                from oopLogin import run_ooplogin
                run_ooplogin(dirPath)
        else:
            from oopLogin import run_ooplogin
            run_ooplogin(dirPath)
        return True
    except Exception as error:
        print('error', error)
        from oopLogin import run_ooplogin
        run_ooplogin(dirPath)
        return False
        # pass


def countProcess(bigfile):
    try:
        dirPath = os.path.dirname(os.path.abspath(__file__))
        from count_entry import CountEntry
        count = CountEntry()
        count.dirPath = dirPath
        count.mainListener()
        return True
    except Exception as error:
        print('Error', error)
    

def runSchedule(integer):
    try:
        dirPath = os.path.dirname(os.path.abspath(__file__))
        from run_scheduler import run_schedule
        run_schedule(dirPath)
        return True
    except Exception as error:
        print('Error', error)
    

def FinalProcess(parsed,pattern,calc_results):
    print('Start of process f')                                                                          
    sleep(10)                                                                       
    print('End of process f')
    return True

def main():
    if platform.system() == "Windows":
        freeze_support()
    pool = Pool(processes=3)
    runMqtt = pool.apply_async(loginProcess, ['largefile'])
    runCountEntry = pool.apply_async(countProcess, [ovalue])
    runSchedul = pool.apply_async(runSchedule, [ovalue])

    pool.close()
    pool.join()


# your __main__ handler goes here
if __name__ == '__main__':
    if platform.system() == "Windows":
        freeze_support()
    main()