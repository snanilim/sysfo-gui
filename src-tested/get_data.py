import psutil
import cpuinfo
import pprint
import re, uuid
import os.path, time, datetime
import platform
import getpass
from requests import get


def _getCpuInfo():
    try:
        cpu_obj: dict = {}
        if platform.system() == 'Linux':
            cpu_info = cpuinfo.get_cpu_info().items()
            for key, value in cpu_info:
                cpu_obj.update({key : value})
            del cpu_obj['flags']
        elif platform.system() == 'Windows':
            import subprocess
            cmd = 'wmic cpu list full'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

            for line in proc.stdout:
                if line.rstrip():
                    pinfo = line.decode().rstrip()
                    pinfo = pinfo.split('=')
                    cpu_obj.update({pinfo[0]:pinfo[1]});
        return cpu_obj
    except Exception as error:
        print('error', error)



def _getMemoryInfo():
    try:
        memory_obj: dict = {}
        memory = psutil.virtual_memory()
        for key in memory._fields:
            value = getattr(memory, key)
            memory_obj.update({key: value})
        return memory_obj
    except Exception as error:
        print('error', error)


def _getDiskInfo():
    try:
        disk_obj: dict = {}
        disk = psutil.disk_usage('/')
        for key in disk._fields:
            value = getattr(disk, key)
            disk_obj.update({key: value})
        return disk_obj
    except Exception as error:
        print('error', error)


def _getProcessInfo():
    try:
        listOfProcObjects = []
        if platform.system() == 'Linux':
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
        
        elif platform.system() == 'Windows':
            import subprocess
            cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            for line in proc.stdout:
                if line.rstrip():
                    # only print lines that are not empty
                    # decode() is necessary to get rid of the binary string (b')
                    # rstrip() to remove `\r\n`
                    # print(line.decode().rstrip())
                    pinfo = line.decode().rstrip()
                    listOfProcObjects.append(pinfo);

        return listOfProcObjects
    except Exception as error:
        print('error', error)



def _getNetworkInfo():
    try:
        net_obj = {}
        net = psutil.net_io_counters()
        for key in net._fields:
            value = getattr(net, key)
            net_obj.update({key: value})
        return net_obj
    except Exception as error:
        print('error', error)


def getStatus():
    return "online"


def getIdleTime(dirPath):
    try:
        if platform.system() == 'Linux':
            idle_time = os.path.getmtime(f"{dirPath}/config/idlefile.txt")
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
    except Exception as error:
        print('error', error)

def mac_addr():
    try:
        mac_addr = hex(uuid.getnode()).replace('0x', '')
        mac_addr = ':'.join(mac_addr[i : i + 2] for i in range(0, 11, 2))
        return mac_addr
    except Exception as error:
        print('error', error)

def gateway_ip():
    try:
        ip = get('https://api.ipify.org').text
        return ip
    except Exception as error:
        print('error', error)

def user_name():
    username = getpass.getuser()
    return username

def get_platform():
    platform_name = platform.system()
    return platform_name

def getData(data):
    try:
        # print('msg', msg.split(','))
        all_info = {}
        

        status_value = data.get("status", "")
        if 'status' in data and status_value == 1:
            # status info
            status_info = getStatus()
            all_info.update({'status': status_info})

        


        # idle_value = data.get("idle", "")
        # if 'idle' in data and idle_value == 1:
        #     # idle info
        #     idle_info = getIdleTime()
        #     all_info.update({'idle': idle_info})


        cpu_value = data.get("cpu", "")
        if 'cpu' in data and cpu_value == 1:
            # cpu info
            cpu_info = _getCpuInfo()
            all_info.update({'cpu_info': cpu_info})

        # return all_info


        memory_value = data.get("memory", "")
        if 'memory' in data and memory_value == 1:
            print('memory')
            # memory info
            memory_info = _getMemoryInfo()
            all_info.update({'memory_info': memory_info})


        disk_value = data.get("disk", "")
        if 'disk' in data and disk_value == 1:
            # disk info
            disk_info = _getDiskInfo()
            all_info.update({'disk_info': disk_info})


        process_value = data.get("process", "")
        if 'process' in data and process_value == 1:
            # process info
            process_info = _getProcessInfo()
            all_info.update({'process_info': process_info})


        network_value = data.get("network", "")
        if 'network' in data and network_value == 1:
            # network info
            network_info = _getNetworkInfo()
            all_info.update({'network_info': network_info})
        
        mac_addr_value = mac_addr()
        all_info.update({'mac_addr': mac_addr_value})

        gateway_ip_value = gateway_ip()
        all_info.update({'gateway_ip': gateway_ip_value})

        get_platform_value = get_platform()
        all_info.update({'platform': get_platform_value})

        user_name_value = user_name()
        all_info.update({'user_name': user_name_value})

        return all_info
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(all_info)
    except Exception as error:
        print('error', error)

