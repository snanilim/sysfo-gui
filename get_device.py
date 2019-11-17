# import win32com.client
import platform


# def getPrinterInfo():
#     try:
#         cpu_obj: dict = {}
#         if platform.system() == 'Linux':
#             pass
#         elif platform.system() == 'Windows':
#             import subprocess
#             cmd = 'wmic printer get name'
#             proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#             print('proc', proc)

#             avoid_list = ['Name', 'Send To OneNote 2013',
#                           'Microsoft XPS Document Writer', 'Microsoft Print to PDF', 'Fax']
#             printer_list = []

#             for line in proc.stdout:
#                 if line.rstrip():
#                     pinfo = line.decode().rstrip()
#                     if pinfo not in avoid_list:
#                         print('pinfo', pinfo)
#                         printer_list.append(pinfo)
#         print('printer_list', printer_list)
#         return printer_list
#     except Exception as error:
#         print('error', error)


# getPrinterInfo()


# def get_usb_device():
#     try:
#         usb_list = []
#         wmi = win32com.client.GetObject("winmgmts:")
#         for usb in wmi.InstancesOf("Win32_USBHub"):
#             print(usb.FriendlyName)
#             # print(usb.description)
#             usb_list.append(usb.description)

#         print(usb_list)
#         return usb_list
#     except Exception as error:
#         print('error', error)


# get_usb_device()


# import os
# os.system('echo list volume > Ravi.txt')
# path1 = os.path.join(os.getcwd(),"Ravi.txt")
# os.system('diskpart /s '+path1+' > logfile.txt')
# path2 = os.path.join(os.getcwd(),"logfile.txt")

# Str = open(path2).read()
# Str = Str.split('\n')
# matching = [s for s in Str if "Removable" in s]

# for i in matching:
#     i = ' '.join(i.split())
#     i = i.split(" ")
#     print(i[3]+"("+i[2]+":)")



# import subprocess, json

# out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId,PresentOnly | ConvertTo-Json}\"")
# j = json.loads(out)
# usb_list = []
# dic = {}
# for dev in j:
#     if dev['Status'] == 'OK':
#         # usb_list.append(dev['FriendlyName'])
#         # print(dev['Class'], dev['FriendlyName'])
#         if dev['Class'] in dic.keys():
#             dic[dev['Class']].append(dev['FriendlyName'])
#         else:
#             dic[dev['Class']] = []
#             dic[dev['Class']].append(dev['FriendlyName'])

# print(dic)
# print(len(usb_list))

listOne = ['USB Root Hub (USB 3.0)', 'Bluetooth', 'High Definition Audio Controller', 'Motherboard resources', 'Motherboard resources', 'Motherboard resources', 'HID-compliant system controller', 'HID-compliant consumer control device', 'Microsoft ACPI-Compliant Control Method Battery', 'ACPI Processor Aggregator', 'Root Print Queue', 'HID Keyboard Device', 'Volume Manager', 'Volume', 'Volume', 'Intel(R) Dynamic Platform and Thermal Framework Manager', 'WAN Miniport (PPPOE)', 'Send To OneNote 2013', 'Microsoft Basic Display Driver', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'ACPI Thermal Zone', 'ACPI Sleep Button', 'Microsoft Wi-Fi Direct Virtual Adapter #3', 'Microsoft Wi-Fi Direct Virtual Adapter #4', 'Fax', 'Legacy device', 'HID-compliant mouse', 'Microsoft RRAS Root Enumerator', 'ICEsound Effects Component', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O SMBUS - 9D23', 'WAN Miniport (PPTP)', 'Microsoft AC Adapter', 'Speakers (Conexant SmartAudio HD)', 'HID-compliant wireless radio controls', 'Microsoft Hyper-V Virtualization Infrastructure Driver', 'High precision event timer', 'WAN Miniport (IKEv2)', 'Composite Bus Enumerator', 'Microsoft Virtual Drive Enumerator', 'TOSHIBA MQ04ABF100', 'System Firmware', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PMC - 9D21', 'Intel(R) Xeon(R) E3 - 1200 v6/7th Gen Intel(R) Core(TM) Host Bridge/DRAM Registers - 5914', 'Microsoft Storage Spaces Controller', 'Microsoft ACPI-Compliant Embedded Controller', 'Intel(R) Serial IO I2C Host Controller - 9D60', 'System timer', 'Intel(R) Serial IO UART Host Controller - 9D27', 'USB2.0 VGA UVC WebCam', 'Volume', 'Microsoft Kernel Debug Network Adapter', 'Generic volume shadow copy', 'Generic volume shadow copy', 'Generic volume shadow copy', 'Generic volume shadow copy', 'PC/AT Enhanced PS/2 Keyboard (101/102-Key)', 'Volume', 'Motherboard resources', 'Microphone (Conexant SmartAudio HD)', 'HID-compliant vendor-defined device', 'Intel(R) Dynamic Platform and Thermal Framework Processor Participant', 'Conexant SmartAudio HD', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Dual Band Wireless-AC 8265', 'UMBus Root Bus Enumerator', 'Charge Arbitration Driver', 'ACPI Lid', 'Microsoft Radio Device Enumeration Bus', 'Microsoft Device Association Root Enumerator', 'ACPI x64-based PC', 'ASUS Wireless Radio Control', 'USB Input Device', 'WAN Miniport (Network Monitor)', 'WAN Miniport (IP)', 'Microsoft Windows Management Interface for ACPI', 'PCI Express Root Complex', 'Generic PnP Monitor', 'Microsoft Print to PDF', 'ACPI Power Button', 'Microsoft ACPI-Compliant System', None, 'Intel(R) Serial IO SPI Host Controller - 9D29', 'Microsoft Basic Render Driver', 'Intel(R) USB 3.0 eXtensible Host Controller - 1.0 (Microsoft)', 'WAN Miniport (SSTP)', 'USB Input Device', 'Microsoft UEFI-Compliant System', 'Intel(R) Display Audio', 'USB Composite Device', 'Trusted Platform Module 2.0', 'ACPI Fixed Feature Button', 'Wi-Fi', 'Volume', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O Thermal subsystem - 9D31', 'Mobile 7th Generation Intel(R) Processor Family I/O LPC Controller (U with iHDCP2.2 Premium) - 9D4E', 'Intel(R) Power Engine Plug-in', 'System CMOS/real time clock', 'Intel(R) 6th Generation Core Processor Family Platform I/O SATA AHCI Controller', 'Motherboard resources', 'I2C HID Device', 'Programmable interrupt controller', 'Microsoft GS Wavetable Synth', 'Intel(R) Management Engine Interface ', 'USB Input Device', 'NDIS Virtual Network Adapter Enumerator', 'Motherboard resources', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PCI Express Root Port #1 - 9D10', 'HID-compliant mouse', 'Intel(R) UHD Graphics 620', 'Microsoft XPS Document Writer', 'Microsoft System Management BIOS Driver', 'HID-compliant vendor-defined device', 'ICEsound Effects Component', 'ELAN WBF Fingerprint Sensor', 'USB Composite Device', 'Intel(R) Serial IO I2C Host Controller - 9D61', 'Microsoft Input Configuration Device', 'Plug and Play Software Device Enumerator', 'Volume', 'ASUS Precision Touchpad', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PCI Express Root Port #6 - 9D15', 'Remote Desktop Device Redirector Bus', 'Intel(R) Wireless Bluetooth(R)', 'Intel(R) PROSet/Wireless WiFi Software', 'HID-compliant mouse', 'WAN Miniport (IPv6)', 'HP LaserJet 4350 PCL6 Class Driver', 'WAN Miniport (L2TP)']
listTwo = ['USB Root Hub (USB 3.0)', 'Bluetooth', 'High Definition Audio Controller', 'Motherboard resources', 'Motherboard resources', 'Motherboard resources', 'HID-compliant system controller', 'HID-compliant consumer control device', 'Microsoft ACPI-Compliant Control Method Battery', 'ACPI Processor Aggregator', 'Root Print Queue', 'HID Keyboard Device', 'Volume Manager', 'Volume', 'Volume', 'Intel(R) Dynamic Platform and Thermal Framework Manager', 'WAN Miniport (PPPOE)', 'Send To OneNote 2013', 'Microsoft Basic Display Driver', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'ACPI Thermal Zone', 'ACPI Sleep Button', 'Microsoft Wi-Fi Direct Virtual Adapter #3', 'Microsoft Wi-Fi Direct Virtual Adapter #4', 'Fax', 'Legacy device', 'HID-compliant mouse', 'Microsoft RRAS Root Enumerator', 'ICEsound Effects Component', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O SMBUS - 9D23', 'WAN Miniport (PPTP)', 'Microsoft AC Adapter', 'Speakers (Conexant SmartAudio HD)', 'HID-compliant wireless radio controls', 'Microsoft Hyper-V Virtualization Infrastructure Driver', 'High precision event timer', 'WAN Miniport (IKEv2)', 'Composite Bus Enumerator', 'Microsoft Virtual Drive Enumerator', 'TOSHIBA MQ04ABF100', 'System Firmware', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PMC - 9D21', 'Intel(R) Xeon(R) E3 - 1200 v6/7th Gen Intel(R) Core(TM) Host Bridge/DRAM Registers - 5914', 'Microsoft Storage Spaces Controller', 'Microsoft ACPI-Compliant Embedded Controller', 'Intel(R) Serial IO I2C Host Controller - 9D60', 'System timer', 'Intel(R) Serial IO UART Host Controller - 9D27', 'USB2.0 VGA UVC WebCam', 'Volume', 'Microsoft Kernel Debug Network Adapter', 'Generic volume shadow copy', 'Generic volume shadow copy', 'Generic volume shadow copy', 'Generic volume shadow copy', 'PC/AT Enhanced PS/2 Keyboard (101/102-Key)', 'Volume', 'Motherboard resources', 'Microphone (Conexant SmartAudio HD)', 'HID-compliant vendor-defined device', 'Intel(R) Dynamic Platform and Thermal Framework Processor Participant', 'Conexant SmartAudio HD', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Dual Band Wireless-AC 8265', 'UMBus Root Bus Enumerator', 'Charge Arbitration Driver', 'ACPI Lid', 'Microsoft Radio Device Enumeration Bus', 'Microsoft Device Association Root Enumerator', 'ACPI x64-based PC', 'ASUS Wireless Radio Control', 'WAN Miniport (Network Monitor)', 'WAN Miniport (IP)', 'Microsoft Windows Management Interface for ACPI', 'PCI Express Root Complex', 'Generic PnP Monitor', 'Microsoft Print to PDF', 'ACPI Power Button', 'Microsoft ACPI-Compliant System', None, 'Intel(R) Serial IO SPI Host Controller - 9D29', 'Microsoft Basic Render Driver', 'Intel(R) USB 3.0 eXtensible Host Controller - 1.0 (Microsoft)', 'WAN Miniport (SSTP)', 'USB Input Device', 'Microsoft UEFI-Compliant System', 'Intel(R) Display Audio', 'USB Composite Device', 'Trusted Platform Module 2.0', 'ACPI Fixed Feature Button', 'Wi-Fi', 'Volume', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O Thermal subsystem - 9D31', 'Mobile 7th Generation Intel(R) Processor Family I/O LPC Controller (U with iHDCP2.2 Premium) - 9D4E', 'Intel(R) Power Engine Plug-in', 'System CMOS/real time clock', 'Intel(R) 6th Generation Core Processor Family Platform I/O SATA AHCI Controller', 'Motherboard resources', 'I2C HID Device', 'Programmable interrupt controller', 'Microsoft GS Wavetable Synth', 'Intel(R) Management Engine Interface ', 'USB Input Device', 'NDIS Virtual Network Adapter Enumerator', 'Motherboard resources', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PCI Express Root Port #1 - 9D10', 'Intel(R) UHD Graphics 620', 'Microsoft XPS Document Writer', 'Microsoft System Management BIOS Driver', 'HID-compliant vendor-defined device', 'ICEsound Effects Component', 'ELAN WBF Fingerprint Sensor', 'USB Composite Device', 'Intel(R) Serial IO I2C Host Controller - 9D61', 'Microsoft Input Configuration Device', 'Plug and Play Software Device Enumerator', 'Volume', 'ASUS Precision Touchpad', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PCI Express Root Port #6 - 9D15', 'Remote Desktop Device Redirector Bus', 'Intel(R) Wireless Bluetooth(R)', 'Intel(R) PROSet/Wireless WiFi Software', 'HID-compliant mouse', 'WAN Miniport (IPv6)', 'HP LaserJet 4350 PCL6 Class Driver', 'WAN Miniport (L2TP)']
listTHree = ['USB Root Hub (USB 3.0)', 'Bluetooth', 'High Definition Audio Controller', 'Motherboard resources', 'Motherboard resources', 'Motherboard resources', 'Microsoft ACPI-Compliant Control Method Battery', 'ACPI Processor Aggregator', 'Root Print Queue', 'Volume Manager', 'Volume', 'Volume', 'Intel(R) Dynamic Platform and Thermal Framework Manager', 'WAN Miniport (PPPOE)', 'Send To OneNote 2013', 'Microsoft Basic Display Driver', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'Intel(R) Dynamic Platform and Thermal Framework Generic Participant', 'ACPI Thermal Zone', 'ACPI Sleep Button', 'Microsoft Wi-Fi Direct Virtual Adapter #3', 'Microsoft Wi-Fi Direct Virtual Adapter #4', 'Fax', 'Legacy device', 'Microsoft RRAS Root Enumerator', 'ICEsound Effects Component', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O SMBUS - 9D23', 'WAN Miniport (PPTP)', 'Microsoft AC Adapter', 'Speakers (Conexant SmartAudio HD)', 'HID-compliant wireless radio controls', 'Microsoft Hyper-V Virtualization Infrastructure Driver', 'High precision event timer', 'WAN Miniport (IKEv2)', 'Composite Bus Enumerator', 'Microsoft Virtual Drive Enumerator', 'TOSHIBA MQ04ABF100', 'System Firmware', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PMC - 9D21', 'Intel(R) Xeon(R) E3 - 1200 v6/7th Gen Intel(R) Core(TM) Host Bridge/DRAM Registers - 5914', 'Microsoft Storage Spaces Controller', 'Microsoft ACPI-Compliant Embedded Controller', 'Intel(R) Serial IO I2C Host Controller - 9D60', 'System timer', 'Intel(R) Serial IO UART Host Controller - 9D27', 'USB2.0 VGA UVC WebCam', 'Volume', 'Microsoft Kernel Debug Network Adapter', 'PC/AT Enhanced PS/2 Keyboard (101/102-Key)', 'Volume', 'Motherboard resources', 'Microphone (Conexant SmartAudio HD)', 'Intel(R) Dynamic Platform and Thermal Framework Processor Participant', 'Conexant SmartAudio HD', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'Intel(R) Dual Band Wireless-AC 8265', 'UMBus Root Bus Enumerator', 'Charge Arbitration Driver', 'ACPI Lid', 'Microsoft Radio Device Enumeration Bus', 'Microsoft Device Association Root Enumerator', 'ACPI x64-based PC', 'ASUS Wireless Radio Control', 'WAN Miniport (Network Monitor)', 'WAN Miniport (IP)', 'Microsoft Windows Management Interface for ACPI', 'PCI Express Root Complex', 'Generic PnP Monitor', 'Microsoft Print to PDF', 'ACPI Power Button', 'Microsoft ACPI-Compliant System', None, 'Intel(R) Serial IO SPI Host Controller - 9D29', 'Microsoft Basic Render Driver', 'Intel(R) USB 3.0 eXtensible Host Controller - 1.0 (Microsoft)', 'WAN Miniport (SSTP)', 'Microsoft UEFI-Compliant System', 'Intel(R) Display Audio', 'Trusted Platform Module 2.0', 'ACPI Fixed Feature Button', 'Wi-Fi', 'Volume', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O Thermal subsystem - 9D31', 'Mobile 7th Generation Intel(R) Processor Family I/O LPC Controller (U with iHDCP2.2 Premium) - 9D4E', 'Intel(R) Power Engine Plug-in', 'System CMOS/real time clock', 'Intel(R) 6th Generation Core Processor Family Platform I/O SATA AHCI Controller', 'Motherboard resources', 'I2C HID Device', 'Programmable interrupt controller', 'Microsoft GS Wavetable Synth', 'Intel(R) Management Engine Interface ', 'NDIS Virtual Network Adapter Enumerator', 'Motherboard resources', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PCI Express Root Port #1 - 9D10', 'Intel(R) UHD Graphics 620', 'Microsoft XPS Document Writer', 'Microsoft System Management BIOS Driver', 'HID-compliant vendor-defined device', 'ICEsound Effects Component', 'ELAN WBF Fingerprint Sensor', 'USB Composite Device', 'Intel(R) Serial IO I2C Host Controller - 9D61', 'Microsoft Input Configuration Device', 'Plug and Play Software Device Enumerator', 'Volume', 'ASUS Precision Touchpad', 'Mobile 6th/7th Generation Intel(R) Processor Family I/O PCI Express Root Port #6 - 9D15', 'Remote Desktop Device Redirector Bus', 'Intel(R) Wireless Bluetooth(R)', 'Intel(R) PROSet/Wireless WiFi Software', 'HID-compliant mouse', 'WAN Miniport (IPv6)', 'HP LaserJet 4350 PCL6 Class Driver', 'WAN Miniport (L2TP)']
# print(list(set(listTwo) - set(listTHree)))

{
'USB':[
      'USB Root Hub (USB 3.0)',
      'Intel(R) USB 3.0 eXtensible Host Controller - 1.0 ',
      'USB Composite Device',
      'USB Composite Device'
   ],
'PrintQueue':[
      'Root Print Queue',
      'Send To OneNote 2013',
      'Fax',
      'Microsoft Print to PDF',
      'Microsoft XPS Document Writer',
      'HP LaserJet 4350 PCL6 Class Driver'
   ],

 'Keyboard':[
      'HID Keyboard Device',
      'PC/AT Enhanced PS/2 Keyboard (101/102-Key)'
   ],
'Mouse':[
      'HID-compliant mouse',
      'HID-compliant mouse'
   ],
'Camera':[
      'USB2.0 VGA UVC WebCam'
   ],
'AudioEndpoint':[
      'Speakers (Conexant SmartAudio HD)',
      'Microphone (Conexant SmartAudio HD)'
   ],

'Display': [
    'Intel(R) UHD Graphics 620'
  ],

'Monitor': [
    'Generic PnP Monitor'
  ],

'Camera':[
      'USB2.0 VGA UVC WebCam'
   ],

'DiskDrive':[
      'TOSHIBA MQ04ABF100'
   ],
'Bluetooth': [
    'Intel(R) Wireless Bluetooth(R)'
  ],
'Biometric': [
    'ELAN WBF Fingerprint Sensor'
  ],

}