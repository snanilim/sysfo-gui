import psutil
import os
import subprocess


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
    try:
        if os.path.exists("D:\programmer\sysfo-gui\src/agent.exe"):
            os.rename("D:\programmer\sysfo-gui\src/agent.exe", "D:\programmer\sysfo-gui\src/agent_old.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)


def rename_new_process():
    try:
        if os.path.exists("D:\programmer\sysfo-gui\src\srdl_new_agent.exe"):
            os.rename("D:\programmer\sysfo-gui\src\srdl_new_agent.exe", "D:\programmer\sysfo-gui\src/agent.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)


def start_new_process():
    try:
        os.startfile('D:\programmer\sysfo-gui\src/agent.exe')
    except Exception as error:
        print('error', error)



def delete_prev_process():
    try:
        if os.path.exists("D:\programmer\sysfo-gui\src/agent_old.exe"):
            os.remove("D:\programmer\sysfo-gui\src/agent_old.exe")
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
