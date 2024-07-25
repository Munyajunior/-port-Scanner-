
import socket

def is_port_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

host_ip = input("Enter host IP: ")
for port in range(1, 1025):  # Scan common ports (1-1024)
    if is_port_open(host_ip, port):
        print(f"Port {port} is open")
