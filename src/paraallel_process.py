from multiprocessing import Pool
from time import sleep   

# all your methods declarations above go here
# (...)

def Process1(largefile):
    import oopLogin
    return True

def Process2(bigfile):
    import data_entry
    return True

def Process3(integer):
    print('Start of process 3')                                                                            
    sleep(10)                                                                       
    print('End of process 3')
    return True

def FinalProcess(parsed,pattern,calc_results):
    print('Start of process f')                                                                            
    sleep(10)                                                                       
    print('End of process f')
    return True

def main():
    pool = Pool(processes=3)
    # runMqtt = pool.apply_async(Process1, ['largefile'])
    runDataEntry = pool.apply_async(Process2, ['largefile'])

    pool.close()
    pool.join()


# your __main__ handler goes here
if __name__ == '__main__':
    main()