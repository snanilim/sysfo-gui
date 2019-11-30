import psutil
import cpuinfo
import pprint
import re, uuid
import os.path, time, datetime, ast
import platform
import getpass
from requests import get
# import win32com.client
import subprocess, json


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
        dps = psutil.disk_partitions(all=True)
        disk_obj: dict = {'total': 0, 'used': 0, 'free': 0, 'percent': 0}
        for i in range(len(dps)):
            dp = dps[i]
            disk = psutil.disk_usage(dp.mountpoint)
            for key in disk._fields:
                value = getattr(disk, key)
                disk_obj[key] = disk_obj.get(key) + value

        # print(disk_obj)
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

def get_version(dirPath):
    fileRead = open(f"{dirPath}/config/version.txt", "r")
    data = fileRead.read()
    data = ast.literal_eval(data)
    version_name = data['version']
    return version_name


def getPrinterInfo():
    try:
        cpu_obj: dict = {}
        if platform.system() == 'Linux':
            pass
        elif platform.system() == 'Windows':
            import subprocess
            cmd = 'wmic printer get name'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            print('proc', proc)

            avoid_list = ['Name', 'Send To OneNote 2013', 'Microsoft XPS Document Writer', 'Microsoft Print to PDF', 'Fax']
            printer_list = []

            for line in proc.stdout:
                if line.rstrip():
                    pinfo = line.decode().rstrip()
                    if pinfo not in avoid_list:
                        print('pinfo', pinfo)
                        printer_list.append(pinfo)
        print('printer_list', printer_list)
        return printer_list
    except Exception as error:
        print('error', error)


def get_machine_id():
    try:
        if platform.system() == 'Linux':
            # machine_id = os.popen("sudo cat /sys/class/dmi/id/product_uuid")
            cmd = 'sudo cat /sys/class/dmi/id/product_uuid'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            for line in proc.stdout:
                machine_id = line.decode().rstrip()
                print('line', machine_id)
            print('machine_id', machine_id)
            return machine_id
        elif platform.system() == 'Windows':
            machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            print(machine_id)
            return machine_id
    except Exception as error:
        print('error', error)


def get_mother_board_info():
    if platform.system() == 'Linux':
        # sudo dmidecode -t 2
        return 'mother_board_info'
    elif platform.system() == 'Windows':
        cmd = 'powershell "gwmi win32_baseboard | FL Product,Manufacturer,SerialNumber,Version'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        mother_board_info = {}

        for line in proc.stdout:
            if line.rstrip():
                pinfo = line.decode().rstrip()
                line_split = pinfo.split(' : ')
                mother_board_info.update({line_split[0].rstrip(): line_split[1]})
        print(mother_board_info)
        return mother_board_info


def get_device_info():
    if platform.system() == 'Linux':
        return 'get_device_info'
    elif platform.system() == 'Windows':
        try:
            out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId,PresentOnly | ConvertTo-Json}\"")
            j = json.loads(out)
            accepted_item = ['USB', 'PrintQueue', 'Keyboard', 'Mouse', 'Camera', 'AudioEndpoint', 'Camera', 'DiskDrive', 'Display', 'Monitor', 'Bluetooth', 'Biometric']
            dic = {}
            for dev in j:
                if dev['Status'] == 'OK':
                    # usb_list.append(dev['FriendlyName'])
                    # print(dev['Class'], dev['FriendlyName'])
                    if dev['Class'] in accepted_item:
                        if dev['Class'] in dic.keys():
                            dic[dev['Class']].append(dev['FriendlyName'])
                        else:
                            dic[dev['Class']] = []
                        dic[dev['Class']].append(dev['FriendlyName'])

            return dic
        except Exception as error:
            print('error', error)




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


        motherboard_value = data.get("motherboard", "")
        if 'motherboard' in data and motherboard_value == 1:
            # network info
            motherboard_info = get_mother_board_info()
            all_info.update({'motherboard_info': motherboard_info})

        device_value = data.get("devices", "")
        if 'devices' in data and device_value == 1:
            # network info
            device_info = get_device_info()
            all_info.update({'device_info': device_info})

        
        machine_id = get_machine_id()
        all_info.update({'machine_id': machine_id})

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


