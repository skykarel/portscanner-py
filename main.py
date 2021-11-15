import scanner

ports = scanner.getOpenPorts("www.google.com", range(1000))
print("Open ports:", ports)
