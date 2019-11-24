# import win32com.client
# import pythoncom
# import os
# # from win32com.shell import shell, shellcon

# # print(shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0))
# # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
# startup_path = f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' # path to where you want to put the .lnk
# path = os.path.join(startup_path, 'agent.lnk')
# target = r'D:\programmer\sysfo-gui\test.py'
# # icon = r'C:\path\to\icon\resource.ico' # not needed, but nice

# shell = win32com.client.Dispatch("WScript.Shell")
# shortcut = shell.CreateShortCut(path)
# shortcut.Targetpath = target
# # shortcut.IconLocation = icon
# shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
# shortcut.save()

# import psutil

# def getDiskInfo():
#     try:
#         dps = psutil.disk_partitions(all=True)
#         disk_obj: dict = {'total': 0, 'used': 0, 'free': 0, 'percent': 0}
#         for i in range(len(dps)):
#             dp = dps[i]
#             disk = psutil.disk_usage(dp.mountpoint)
#             for key in disk._fields:
#                 value = getattr(disk, key)
#                 disk_obj[key] = disk_obj.get(key) + value

#         print(disk_obj)
#         return disk_obj
#     except Exception as error:
#         print('error', error)
# getDiskInfo()
# from __future__ import print_function 3309881036
# import psutil

# dps = psutil.disk_partitions(all=True)

# disk_obj: dict = {'total': 0, 'used': 0, 'free': 0, 'percent': 0}
# for i in range(len(dps)):
#     dp = dps[i]
#     print('dp', dp)
#     disk = psutil.disk_usage(dp.mountpoint)
#     for key in disk._fields:
#         value = getattr(disk, key)
#         disk_obj[key] = disk_obj.get(key) + value

# print(disk_obj)




# import subprocess
# machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
# print(machine_id)

# def get_mother_board_info():
#     cmd = 'powershell "gwmi win32_baseboard | FL Product,Manufacturer,SerialNumber,Version'
#     proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

#     mother_board_info = {}

#     for line in proc.stdout:
#         if line.rstrip():
#             pinfo = line.decode().rstrip()
#             line_split = pinfo.split(' : ')
#             mother_board_info.update({line_split[0].rstrip(): line_split[1]})
#     print(mother_board_info)
#     return mother_board_info

