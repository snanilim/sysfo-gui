from multiprocessing import Pool
from time import sleep
import os, ast, json
import datetime
from hepler import *

# all your methods declarations above go here
# (...)

ovalue = 0

def loginProcess(largefile):
    try:
        data = has_data_on_file()
        if data:
            token_obj = get_dec_data(data)
            print('token_obj', token_obj)
            token_obj = token_obj.replace("'", "\"")
            token_obj = eval(token_obj)
            token_value = token_obj['auth_token']
            print('token_obj', token_value)

            if token_value:
                print('hello')
                from client_mqtt import MQTTClient
                client = MQTTClient()
                client.on_loop_forever()
            else:
                import oopLogin
        else:
            import oopLogin
        return True
    except Exception as error:
        print('error', error)
        import oopLogin
        return False
        # pass


def countProcess(bigfile):
    from count_entry import CountEntry
    count = CountEntry()
    count.mainListener()
    return True

def runSchedule(integer):
    from run_scheduler import run_schedule
    run_schedule()
    return True

def FinalProcess(parsed,pattern,calc_results):
    print('Start of process f')                                                                          
    sleep(10)                                                                       
    print('End of process f')
    return True

def main():
    pool = Pool(processes=3)
    runMqtt = pool.apply_async(loginProcess, ['largefile'])
    # runCountEntry = pool.apply_async(countProcess, [ovalue])
    # runSchedul = pool.apply_async(runSchedule, [ovalue])

    pool.close()
    pool.join()


# your __main__ handler goes here
if __name__ == '__main__':
    main()