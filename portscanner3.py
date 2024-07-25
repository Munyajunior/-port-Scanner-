import socket
import threading
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Set a timeout for faster scanning
    try:
        s.connect((host_ip, port))
        print(f"{GREEN}Port {port} is open{RESET}")
    except:
        #print(f"{RED}Port {port} is closed{RESET}")
        pass

host_ip = input("Enter host IP: ")
for port in range(1, 100001):  # Scan a large range of ports (adjust as needed)
    t = threading.Thread(target=port_scan, kwargs={"port": port})
    t.start()

