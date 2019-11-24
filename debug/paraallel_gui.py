from multiprocessing import Pool, freeze_support
from time import sleep
import os, ast, json


# all your methods declarations above go here
# (...)

ovalue = 0

def loginProcess(largefile):
    try:
        import gui_gui
        print('okkk')
        return True
    except Exception as error:
        print('error', error)
        # pass




def main():
    freeze_support()
    pool = Pool(processes=3)
    a = pool.apply_async(loginProcess, ['bob'])
    b = pool.apply_async(loginProcess, ['bob'])

    pool.close()
    pool.join()


# your __main__ handler goes here
if __name__ == '__main__':
    freeze_support()
    main()