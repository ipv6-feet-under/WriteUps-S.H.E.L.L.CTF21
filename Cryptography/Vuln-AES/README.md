![S.H.E.L.L.CTF](../../banner.png)

# Challenge Name
```
This implementation of AES is breakable, but how ?
I set it up at : nc 34.92.214.217 8885

Note : May need to use automation scripts.
Flag format : shell{} and its 16 chars in length
```
We are given a netcat address and port and also the [script](encrypt.py) that is running on it.





sixteen byte AES
|s|i|x|t|e|e|n| |b|y|t|e| |A|E|S|X|X|
|---|---|---|
|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|


[Final Script](vulnaes.py)
```py
from pwn import *

host = '34.92.214.217'
port = 8885

flag = 'shell{'

while True:
    t = remote(host, port)
    payload = "0"*(15-len(flag))
    t.recvuntil(':')
    t.sendline(payload)
    zwischenergebnis = t.recvall()
    zwischenergebnis = base64.b64decode(zwischenergebnis).hex()
    zwischenergebnis = zwischenergebnis[33:-32]

    for i in range(45, 125):
        print('Testing Character:' + chr(i))
        print("Flag: ", flag)
        t = remote(host, port)
        t.recvuntil(': ')
        print('sending....: ' + payload + flag + chr(i))
        t.sendline(payload + flag + chr(i))
        encoded = t.recvall()
        encoded = base64.b64decode(encoded).hex()
        print('ich vergleiche: ' + encoded[33:-32] + ' mit: ' + zwischenergebnis)

        if encoded[33:-32] == zwischenergebnis:
            flag += chr(i)
            print("Flag: ", flag)
            break
    if len(flag) == 16:
        break
print(flag)
```