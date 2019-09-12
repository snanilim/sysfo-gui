import psutil
import cpuinfo
import pprint
import re, uuid
import os.path, time, datetime
import platform
from requests import get


def _getCpuInfo():
    cpu_obj: dict = {}
    cpu_info = cpuinfo.get_cpu_info().items()
    for key, value in cpu_info:
        cpu_obj.update({key : value})
    del cpu_obj['flags']
    return cpu_obj



def _getMemoryInfo():
    memory_obj: dict = {}
    memory = psutil.virtual_memory()
    for key in memory._fields:
        value = getattr(memory, key)
        memory_obj.update({key: value})
    return memory_obj


def _getDiskInfo():
    disk_obj: dict = {}
    disk = psutil.disk_usage('/')
    for key in disk._fields:
        value = getattr(disk, key)
        disk_obj.update({key: value})
    return disk_obj


def _getProcessInfo():
    # for x in psutil.process_iter():
    #     print(x)
    # process = [p.info for p in psutil.process_iter(attrs=['name', 'username'])]
    # return process
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
 
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
 
    return listOfProcObjects



def _getNetworkInfo():
    net_obj = {}
    net = psutil.net_io_counters()
    for key in net._fields:
        value = getattr(net, key)
        net_obj.update({key: value})
    return net_obj


def _getStatus():
    return "online"


def _getIdleTime():
    if platform.system() == 'Linux':
        idle_time = os.path.getmtime("idlefile.txt")
        return idle_time
    elif platform.system() == 'Windows':
        from ctypes import Structure, windll, c_uint, sizeof, byref
        
        class LASTINPUTINFO(Structure):
            _fields_ = [
                ('cbSize', c_uint),
                ('dwTime', c_uint),
            ]

        def get_idle_duration():
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = sizeof(lastInputInfo)
            windll.user32.GetLastInputInfo(byref(lastInputInfo))
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            sec = millis / 1000.0
            ctime = datetime.datetime.now() - datetime.timedelta(seconds = sec)
            unixtime = time.mktime(ctime.timetuple())
            return unixtime
            # return millis / 1000.0

        return get_idle_duration()


def mac_addr():
    mac_addr = hex(uuid.getnode()).replace('0x', '')
    mac_addr = ':'.join(mac_addr[i : i + 2] for i in range(0, 11, 2))
    return mac_addr

def gateway_ip():
    ip = get('https://api.ipify.org').text
    return ip

def getRegData():
    reg_info = {}
    status_info = _getStatus()
    reg_info.update({'status': status_info})

    # cpu info
    cpu_info = _getCpuInfo()
    reg_info.update({'cpu_info': cpu_info})


    # memory info
    memory_info = _getMemoryInfo()
    reg_info.update({'memory_info': memory_info})


    # disk info
    disk_info = _getDiskInfo()
    reg_info.update({'disk_info': disk_info})


    return reg_info


