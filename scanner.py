# Import modules required for networking and time tracking
import socket
from datetime import datetime
# Create a reusable function to scan a single port on the target
def scan_port(target, port):
    scanner = socket.socket()
    # Set timeout so closed ports respond faster and do not slow the scan
    scanner.settimeout(0.5)
    result = scanner.connect_ex((target, port))
    if result == 0:
        try:
            # Try to identify the common service running on the open port
            service = socket.getservbyport(port)
        except:
            service = 'Unknown'
        print(f'Port {port} is open - {service}')
    scanner.close()
target = input('Enter Target: ')
start_time = datetime.now()
print('-' * 50)
print(f'Scanning target: {target}')
print('Scanning started...')
print(f'Time started: {start_time}')
print('-' * 50)
for port in range(1, 101):
    scan_port(target, port)
print('-' * 50)
print("Scanning completed.")
end_time = datetime.now()
total_time = end_time - start_time
print(f'Total scan time = {total_time}')
