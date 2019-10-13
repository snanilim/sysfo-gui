import subprocess

try:
    subprocess.Popen('E:\programmer\sysfo-gui\debug\gui_gui.exe')
    subprocess.Popen(['E:\programmer\sysfo-gui\debug\gui_gui_2.exe'])
except Exception as error:
    print('error', error)
