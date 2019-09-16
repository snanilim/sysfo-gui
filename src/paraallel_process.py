from multiprocessing import Pool
from time import sleep   

# all your methods declarations above go here
# (...)

ovalue = 0

def loginProcess(largefile):
    import oopLogin
    return True

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
    runCountEntry = pool.apply_async(countProcess, [ovalue])
    runSchedul = pool.apply_async(runSchedule, [ovalue])

    pool.close()
    pool.join()


# your __main__ handler goes here
if __name__ == '__main__':
    main()