# _FuzzerV1:

"""
INFORMATION ABOUT THE SCRIPT
____________________________

Fuzzer (Vulnerability research)

_____________________________
"""

#!/usr/bin/python3
from socket import *

buffer = ["A"]
counter = 100

while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter += 200

for string in buffer:
    print(f"[+] Fuzzing with {len(string)} bytes")
    s = socket(AF_INET,SOCK_STREAM)
    conn = s.connect(("192.168.1.22", 110))

    s.recv(1024)
    s.send('User \r\n'.encode())
    s.recv(1024)

    text = 'pass ' + string + '\r\n'
    s.send(text.encode())
