import socket 
from ping3 import ping
import psutil
import ipaddress 
import regex
class myscan:
    def __init__(self, address=None):
        self.address = address
        self.ip_list = []

    def get_ip_address(self):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        self.address = ip_addr
        return self.address
    
    def get_netmask(self):
        interfaces = psutil.net_if_addrs()
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address == self.address:
                    return addr.netmask
        return None

    def get_usable_ip(self):
        self.get_ip_address()
        netmask = self.get_netmask()
        if netmask:
            network = ipaddress.IPv4Network(f'{self.address}/{netmask}', strict=False)
            self.ip_list = list(network.hosts())
            return self.ip_list
        else:
            return []

my_ip = myscan()
useip = list(my_ip.get_usable_ip())
