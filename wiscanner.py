import socket 
from ping3 import ping
import psutil
import ipaddress 
import re

class color:
   GREEN = '\033[92m'  
   RED = '\033[91m'    
   END = '\033[0m'     

class myscan:
    def __init__(self, address=None):
        self.address = address
        self.ip_list_blob= []
        self.ip_list = []
        self.available_ips = []
        self.available_ports = {}
    
    #gives the host address
    def get_ip_address(self):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        self.address = ip_addr
        return self.address
    #gets the netmask
    def get_netmask(self):
        interfaces = psutil.net_if_addrs()
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address == self.address:
                    return addr.netmask
        return None

    #regex to detect the pattern
    def detect_ip(self,ip_as_text):
        pattern = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",ip_as_text);
        return pattern.group(0) if pattern else None
    
    #gets the usable ip, no i/p needed
    def get_usable_ip(self):
        self.get_ip_address()
        netmask = self.get_netmask()
        if netmask:
            network = ipaddress.IPv4Network(f'{self.address}/{netmask}', strict=False)
            self.ip_list_blob = list(network.hosts())
            for address in self.ip_list_blob:
                detected_ip = self.detect_ip(str(address))
                if detected_ip:
                    self.ip_list.append(detected_ip)
            return self.ip_list
        else:
            return []
    
    #gets the available ip
    def scan_network(self):
        useable_ip = list(self.get_usable_ip())   
        for address in useable_ip:
            response = ping(address,timeout=1)
            #print(f"Pinging IP {address} -> Response {response} ")
            if response is not None:
                self.available_ips.append(address)
                #print(f"IP:{address} available")
            else:
                continue
        return self.available_ips
    
    #scans if the port is available
    def scan_ports(self,address):
        ports = [22, 23, 25, 53, 80, 110, 143, 443, 445, 587, 3389, 3306, 5432, 5900]
        #sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        avail_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            #print(f"Checking port{port} of {address}")
            result = sock.connect_ex((address,port))
            if result == 0:
                #print(f"Port {port} available for {address}")
                avail_ports.append(port)
            else:
                continue
            sock.close()
        return avail_ports

    #gets the available ips and store it in a dictionary
    def get_avail_ports(self):
        self.scan_network()
        #avail_port = []
        for ip in self.available_ips:
            self.available_ports[ip] = self.scan_ports(ip)
        return self.available_ports





my_ip = myscan()
#useip = list(my_ip.get_usable_ip())
#print(useip)
ports = my_ip.get_avail_ports()
for key,values in ports.items():
    print(f"In IP {color.GREEN}{key}{color.END} port {color.RED}{values}{color.END} available")
