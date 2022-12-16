import platform
import cpuinfo.cpuinfo as cpuinfo
import psutil
import socket


class Computer():
    powerSupply = ""
    _cpu = ""
    _cpuSpeed = 0.0
    _ram = 0
    _os = "Test"
    _ip = "Test"

    def __init__(self,cpu, cpuSpeed, psu, ram, os, ip):
        self.powerSupply = psu
        self._cpu = cpu
        self._cpuSpeed = cpuSpeed
        self._os = os
        self._ram = ram
        self._ip = ip
        
    def getInfo(self):
        print("-----------------------------------------------")
        print("PowerSupply:",self.powerSupply)
        print("CPU:",self._cpu)
        print("CPUSpeed:",self._cpuSpeed, "MHz")
        print("Betriebssystem:",self._os)
        print("RAM:",self._ram,"GB")
        print("IP:",self._ip)
        print(2 * "\n")

        
Specs = Computer(cpuinfo.get_cpu_info()['brand_raw'],(psutil.cpu_freq().max),"Hamsterrad", (round((psutil.virtual_memory().total)/1024.0/1024.0/1024.01)), platform.platform(), socket.gethostbyname(socket.gethostname()))




'''     Systemabfragen
        cpu = cpuinfo.get_cpu_info()['brand_raw']
        cpuSpeed = (psutil.cpu_freq().max)
        os = platform.platform()
        ram = (round((psutil.virtual_memory().total)/1024.0/1024.0/1024.01))
        ip = socket.gethostbyname(socket.gethostname())
'''