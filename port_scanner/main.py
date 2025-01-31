import socket
import sys
import pyfiglet

# Display banner
banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

# Get the target from user input
target = input("Enter host to scan: ")
try:
    host = socket.gethostbyname(target)
except socket.gaierror:
    print(f"Error: Unable to resolve host {target}. Exiting.")
    sys.exit()

print(f"Target: {target}")
print(f"Host IP: {host}")

# Scan ports from 1 to 1024
for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.001) 
    result = sock.connect_ex((host, port))  
    if result == 0:
        try:
            
            print(f"Port {port}: Open (Service: {socket.getservbyport(port, 'tcp')})")
        except:
            print(f"Port {port}: Open (Service: Unknown)")
    sock.close()  
