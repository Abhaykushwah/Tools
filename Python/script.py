import nmap

scanner = nmap.PortScanner()

print(" This Nmap script is created by Abhay")
ip_addr = input("Please Enter IP address you want to scan : ")
print("You enter th3 following addr to scan ", ip_addr)

resp = int(input(""" \n Please enter the type of scan you want to run 
            1) SYN ACK scan
            2) UDP scan
            3) Comprehensive scan
            ---------->>>"""))
print("you have selected :", resp )
print(type(resp))
def en_verbose():
    global ip_addr
    verbose = str(input("Do you want to enable verbosity [Y/N] :"))
    if verbose == 'Y' or verbose == 'y':
        PASS
        ip_addr == ip_addr + ' -v'
        # en_verbose = True
    elif verbose == 'N' or verbose == 'n':
        # en_verbose = False
        PASS
    else:
        verbose = ("Wrong input formate, please answer in Y/N : ")
        en_verbose()
# en_verbose()
if resp == 1:
    print("NMAP version ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-sS')
    ## printing scan info 
    print(scanner.scaninfo)
    print("Ip addr status : ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports are : ", scanner[ip_addr]['tcp'].keys())

elif resp == 2:
    print("NMAP version ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-sU')
    ## printing scan info 
    print(scanner.scaninfo)
    print("Ip addr status : ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports are : ", scanner[ip_addr]['udp'].keys())    
    
elif resp == 3:
    print("NMAP version ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-sS -sV -sC -A -O')
    ## printing scan info 
    print(scanner.scaninfo)
    print("Ip addr status : ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports are : ", scanner[ip_addr]['tcp'].keys())
else :
    print("Don/'t be funny, at work...  :-(/'")