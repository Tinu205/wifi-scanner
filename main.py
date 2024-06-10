import socket
from ping3 import ping, verbose_ping
import psutil

ip_list=[]

def get_ip_address():
    # Get the hostname
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return ip_addr

def ip_split():
    ip = get_ip_address()
    x = ip.split(".")
    x = x[0:3]
    return x

def get_ping_response(ip):
    response_time = ping(ip)
    if response_time is not None:
        ip_list.append(ip)

if __name__ == "__main__":
    print(get_ip_address())
    ip = ip_split()
    
    for i in range(1,255):
        print(f"Entering the loop at ip{i} ")

        joint_ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{i}"
        get_ping_response(joint_ip)
    print(ip_list)
    
    
'''
    for host in ip_list:
        name = socket.gethostbyaddr(host)
        print(name[0])
    
'''
