import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("NORMAL SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:

        target = socket.gethostbyname(sys.argv[1])
else:
        print("Invalid amount of Argument")

#Banner
print("+" * 60)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("+" * 60)

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

                # returns an error indicator
        result = s.connect_ex((target,port))
       # print(result)
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
                print("\n Exiting Program !!!!")
                sys.exit()
except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()
