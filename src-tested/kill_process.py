import psutil
import os
import subprocess


def kill_process():
    try:
        PROCNAME = "paraallel_process.exe"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
    except Exception as error:
        print('error', error)


def rename_prev_process():
    try:
        if os.path.exists("E:\programmer\sysfo-gui\src\paraallel_process.exe"):
            os.rename("E:\programmer\sysfo-gui\src\paraallel_process.exe", "E:\programmer\sysfo-gui\src\paraallel_process_old.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)


def rename_new_process():
    try:
        if os.path.exists("E:\programmer\sysfo-gui\src\paraallel_process2.exe"):
            os.rename("E:\programmer\sysfo-gui\src\paraallel_process2.exe", "E:\programmer\sysfo-gui\src\paraallel_process.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)


def start_new_process():
    try:
        os.startfile('E:\programmer\sysfo-gui\src\paraallel_process.exe')
    except Exception as error:
        print('error', error)



def delete_prev_process():
    try:
        if os.path.exists("E:\programmer\sysfo-gui\src\paraallel_process_old.exe"):
            os.remove("E:\programmer\sysfo-gui\src\paraallel_process_old.exe")
        else:
            print('File does not exists')
    except Exception as error:
        print('error', error)

if __name__ == '__main__':
    kill_process()
    rename_prev_process()
    rename_new_process()
    start_new_process()
    delete_prev_process()

