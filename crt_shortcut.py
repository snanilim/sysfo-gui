import win32com.client
import pythoncom
import os
# from win32com.shell import shell, shellcon

# print(shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0))
# pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
startup_path = f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' # path to where you want to put the .lnk
path = os.path.join(startup_path, 'agent.lnk')
target = r'D:\programmer\sysfo-gui\test.py'
# icon = r'C:\path\to\icon\resource.ico' # not needed, but nice

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
# shortcut.IconLocation = icon
shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()
