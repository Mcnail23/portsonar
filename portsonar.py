#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def print_banner():
    banner = r"""
============================================================
  ____   ___  ____ _____ ____   ___  _   _     _     ____  
 |  _ \ / _ \|  _ \_   _/ ___| / _ \| \ | |   / \   |  _ \ 
 | |_) | | | | |_) || | \___ \| | | |  \| |  / _ \  | |_) |
 |  __/| |_| |  _ < | |  ___) | |_| | |\  | / ___ \ |  _ < 
 |_|    \___/|_| \_\|_| |____/ \___/|_| \_\|_/   \_\_| \_\\
                                                            
          DEVELOPED BY: SUDAIS AHMAD DURANI
============================================================
    """
    print(banner)

def scan_ports(target_host, ports_to_scan):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("\n[-] Error: Hostname could not be resolved.")
        sys.exit(1)

    print(f"[*] Target IP resolved: {target_ip}")
    print(f"[*] Scan initiated at: {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
    print("=" * 55)
    print(f"{'PORT':<10}{'STATE':<15}{'SERVICE':<20}")
    print("=" * 55)

    open_ports_count = 0

    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        # Connect_ex returns an error code instead of throwing an exception
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            try:
                service_name = socket.getservbyport(port, "tcp")
            except:
                service_name = "unknown"
                
            print(f"{port:<10}{'OPEN':<15}{service_name:<20}")
            open_ports_count += 1
            
        s.close()

    print("=" * 55)
    print(f"[*] PortSonar scan complete. Found {open_ports_count} open ports.")

if __name__ == "__main__":
    print_banner()

    if len(sys.argv) < 2:
        print("[-] Error: Missing target host.")
        print("Usage: python3 portsonar.py <Target_IP_or_Domain>")
        print("Example: python3 portsonar.py 10.75.215.102")
        sys.exit(1)

    target = sys.argv[1]
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 8080]
    
    scan_ports(target, common_ports)
