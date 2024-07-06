#!/usr/bin/python3

import socket
# import nmap

# scanner = nmap.PortScanner()
# s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET6)
# s.settimeout(5)


def is_valid_hostname(hostname):
    try:
        socket.getaddrinfo(hostname, None)
        return True
    except socket.gaierror:
        return False

def is_valid_ip(ip):
    try:
        socket.inet_pton(socket.AF_INET6 if ':' in ip else socket.AF_INET, ip)
        return True
    except socket.error:
        return False
    
def get_open_ports(target, port_range, verbose=False):

    if is_valid_hostname(target):
        target_type = "hostname"
    elif is_valid_ip(target):
        target_type = "IP address"
    else:
        return "Error: Invalid hostname" if ':' not in target else "Error: Invalid IP address"

    openPorts_Services = []
    # closedPorts = []
            
    for port in range(port_range[0], port_range[1]):
        print("NEW PORT ------------------------------------->>>>>>>>>>>>>>>>")
        if s.connect_ex((target, port)):
            # closedPorts.append([port, "The port is closed"])
            pass
        else:
            ipAddress, *_ = s.getpeername()
            service_name = ports_and_services.get(port, "Not Defined")

            print("ip address// servicename: --> ", ipAddress, service_name)

            hostname, *_ = socket.gethostname()
           
            openPorts_Services.append([port, service_name])

    print("ending ------------------------------------->>>>>>>>>>>>>>>>")
       
    if verbose:
        if openPorts_Services:
            formatedString = ""
            if target_type == "hostname":
                hostname = target
                print("target_type// target: --> ", target_type, target)
            elif target_type == "IP address":
                ipAddress = target
                print("target_type// target: --> ", target_type, target)
                
            formatedString = f"Open ports for {hostname} ({ipAddress})\nPORT     SERVICE\n"
            for port, service in openPorts_Services:
                formatedString += f"{port}      {service}\n"

            return formatedString

    if not openPorts_Services:
        openPorts_Services = "There are no open ports in the selected range"
    return openPorts_Services
    # return formated_String if formated_String else openPorts_Services        

# host = "www.stackoverflow.com"

ports_and_services = {
    7: 'echo',
    20: 'ftp',
    21: 'ftp',
    22: 'ssh',
    23: 'telnet',
    25: 'smtp',
    43: 'whois',
    53: 'dns',
    67: 'dhcp',
    68: 'dhcp',
    80: 'http',
    110: 'pop3',
    123: 'ntp',
    137: 'netbios',
    138: 'netbios',
    139: 'netbios',
    143: 'imap4',
    443: 'https',
    513: 'rlogin',
    540: 'uucp',
    554: 'rtsp',
    587: 'smtp',
    873: 'rsync',
    902: 'vmware',
    989: 'ftps',
    990: 'ftps',
    1194: 'openvpn',
    3306: 'mysql',
    5000: 'unpn',
    8080: 'https-proxy',
    8443: 'https-alt'
}




# host = "2001:41d0:8:ccd8:137:74:187:101"
host = "freecodecamp.com"
print(get_open_ports(host, [20, 23], True))

