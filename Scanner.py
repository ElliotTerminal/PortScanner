#!/usr/bin/python3
# ToolName   : Scanner.py
# Author     : ElliotTerminal
# License    : GPL V3
# Copyright  : ElliotTerminal (2022-2023)
# Github     : https://github.com/ElliotTerminal
# Description: PortScanner is a port scanning tool
# Language   : Python
# If you copy open source code, consider giving credit

import socket
import sys
import time
import threading

usage = "Usage -> python3 portscanner.py (TARGET) (START_PORT) (END_PORT)"

print(" ______ ___________ _____   _____ _____   ___   _   _  _   _  ___________  ")
print(" | ___ \  _  | ___ \_   _| /  ___/  __ \ / _ \ | \ | || \ | ||  ___| ___ \ ")
print(" | |_/ / | | | |_/ / | |   \ `--.| /  \// /_\ \|  \| ||  \| || |__ | |_/ / ")
print(" |  __/| | | |    /  | |    `--. \ |    |  _  || . ` || . ` ||  __||    /  ")
print(" | |   \ \_/ / |\ \  | |   /\__/ / \__/\| | | || |\  || |\  || |___| |\ \  ")
print(" \_|    \___/\_| \_| \_/   \____/ \____/\_| |_/\_| \_/\_| \_/\____/\_| \_| ")
print("                                                        By - ElliotTerminal")

start_time = time.time()

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Rsolution Error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Target ....",target)

def scan_port(port):
    #print("Scanning Port: ", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    conn = s.connect_ex((target, port))
    if(not conn):
        print("Port {} is OPEN".format(port))
    s.close()

for port in range(start_port, end_port+1):
    
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()

end_time = time.time()
print("Time Elapsed: ", end_time - start_time, "s")
