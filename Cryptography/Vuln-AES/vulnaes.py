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
