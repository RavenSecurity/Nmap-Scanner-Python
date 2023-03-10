import nmap

nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
scanner = nmap.PortScanner(nmap_search_path=nmap_path)

print("\n")

print("""                              
  ____   _____ _____  ______  
 /    \ /     \\__  \ \____ \ 
|   |  \  Y Y  \/ __ \|  |_> >
|___|  /__|_|  (____  /   __/ 
     \/      \/     \/|__|     """ , scanner.nmap_version())

print("\n")

ip_addr = input("Please enter the IP address you want to scan: ")
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) TCP Syn (Stealth) Scan
                2) TCP ACK scan
                3) TCP connect scan
                4) UDP Scan
                5) IP protocol scan
                6) Comprehensive Scan \n""")

print("\n")


if resp == '1':
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2' :
    scanner.scan(ip_addr, '1-1024', '-v -sA')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '3' :
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '4' :
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '5':
    print("Please enter a valid option")

# I've fixed this issue in the beginning but it came back after the TCP ACK update:
# nmap.nmap.PortScannerError: 'nmap program was not found in path. PATH 
# What I tried to resolve the issue:
# - sudo apt install nmap
