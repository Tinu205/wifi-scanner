import socket 
import psutil
import ipaddress 
import netifaces
from scapy.all import ARP, Ether, srp

class color:
   GREEN = '\033[92m'  
   RED = '\033[91m'    
   END = '\033[0m'     

class myscan:
    def __init__(self, network=None):
        self.network = network
        self.available_ips = []
        self.available_ports = {}
   
    def get_network_ip(self):
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][1]
        addrs = netifaces.ifaddresses(default_gateway)
        ip_info = addrs[netifaces.AF_INET][0]
        interface = ipaddress.IPv4Interface(f"{ip_info['addr']}/{ip_info['netmask']}")
        network = interface.network
        self.network = str(network)

    def scan_network(self):
        self.get_network_ip()
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=self.network), timeout=2, verbose=False)
        self.available_ips = [received.psrc for sent, received in ans]
        #print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%")))
        return self.available_ips

    def scan_ports(self, address):
        ports = [22, 23, 25, 53, 80, 110, 143, 443, 445, 587, 3389, 3306, 5432, 5900]
        avail_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((address, port))
            if result == 0:
                avail_ports.append(port)
            sock.close()
        return avail_ports

    def get_avail_ports(self):
        self.scan_network()
        for ip in self.available_ips:
            self.available_ports[ip] = self.scan_ports(ip)
        return self.available_ports

# Create an instance of myscan
my_ip = myscan()


available_ips = my_ip.scan_network()
print(f"Available IPs:")
for ip in available_ips:
    print(f"{ip}")

ports = my_ip.get_avail_ports()
for key, values in ports.items():
    print(f"In IP {color.GREEN}{key}{color.END} port {color.RED}{values}{color.END} available")

