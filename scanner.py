#!/usr/bin/python3
import socket #library to use
import subprocess
import sys
from ports import ports_and_services

def getOpenPorts(target, portRange):
    openPorts = []
    #Obtener el host con socket
    IPadrr = socket.gethostbyname(target)
    print("-"*30 + " scanning " + "-"*30)
    print("target ip adress: " + IPadrr)
    print("fqdn: "+socket.getfqdn(target)) #full qualified domain name
    
    
    print("\nscanning... ")
    #hacer un loop sobre el rango de puertos
    try:
        for port in portRange:
    
            #abrir el socket determinado
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            #verificar si se conecta
            result = sock.connect_ex((IPadrr, port))
    
            #si se conecta agregarlo al array
            if result == 0:
                openPorts.append(port)
            sock.close()
    except KeyboardInterrupt:
        print(" You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    return openPorts

