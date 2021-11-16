import scanner
import ports #ports_and_services

ports = scanner.getOpenPorts("www.google.com", range(24,26))
print("\nPuertos/Servicios")
for i in ports:
    print(" " + str(i) + " " + ports_and_services[i])
#print("Open ports:", ports)
