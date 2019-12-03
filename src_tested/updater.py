import psutil
import os, sys
import subprocess


if getattr(sys, 'frozen', False):
    dirPath = os.path.dirname(sys.executable)
elif __file__:
    dirPath = os.path.dirname(__file__)


def kill_process():
    try:
        PROCNAME = "agent.exe"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
    except Exception as error:
        print('error', error)


def rename_prev_process():
    print('dirpath', dirPath)
    try:
        if os.path.exists(f"{dirPath}/agent.exe"):
            os.rename(f"{dirPath}/agent.exe", f"{dirPath}/agent_old.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)


def rename_new_process():
    try:
        if os.path.exists(f"{dirPath}/srdl_new_agent.exe"):
            os.rename(f"{dirPath}/srdl_new_agent.exe", f"{dirPath}/agent.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)


def start_new_process():
    try:
        os.startfile(f'{dirPath}/agent.exe')
    except Exception as error:
        print('error', error)



def delete_prev_process():
    try:
        if os.path.exists(f"{dirPath}/agent_old.exe"):
            os.remove(f"{dirPath}/agent_old.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)

if __name__ == '__main__':
    delete_prev_process()
    kill_process()
    rename_prev_process()
    rename_new_process()
    start_new_process()
    delete_prev_process()

