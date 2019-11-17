import win32com.client
import pythoncom
import os


def has_data_on_file(dirPath):
    try:
        fileRead = open(f"{dirPath}/config/conf-01.txt", "r")
        data = fileRead.read()
        return data
    except Exception as error:
        print('error', error)
    

def get_dec_data(data):
    try:
        def normalize(str):
            str = str.replace(' ', '')
            return " ".join(str[i:i+8] for i in range(0, len(str), 8))
        def dec(str):
            str = normalize(str)
            return ''.join(chr(int(binary, 2)) for binary in str.split(' '))

        dec_data = dec(str(data))
        return dec_data
    except Exception as error:
        print('error', error)



def save_enc_data(token_obj, dirPath):
    try:
        fileWrite = open(f"{dirPath}/config/conf-01.txt", "w")
        def enc(str):
            return ' '.join(bin(ord(char)).split('b')[1].rjust(8, '0') for char in str)

        token_obj = enc(str(token_obj))
        fileWrite.write(token_obj)
        fileWrite.close()
        return True
    except Exception as error:
        print('error', error)


def crt_shortcut_save(dirPath):
    try:
        # from win32com.shell import shell, shellcon

        # print(shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0))
        # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
        startup_path = f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' # path to where you want to put the .lnk
        path = os.path.join(startup_path, 'agent.lnk')
        target = f'{dirPath}/paraallel_process.py'
        # icon = r'C:\path\to\icon\resource.ico' # not needed, but nice

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        # shortcut.IconLocation = icon
        shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
        shortcut.save()
    except Exception as error:
        print('error', error)
