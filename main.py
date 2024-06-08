import socket

host = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(r"{host}->{ip}")
