from multiprocessing import Process, freeze_support
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
    p = Process(target=loginProcess, args=('bob',))
    p.start()
    p.join()


# your __main__ handler goes here
if __name__ == '__main__':
    freeze_support()
    main()