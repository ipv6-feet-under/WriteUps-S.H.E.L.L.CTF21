![S.H.E.L.L.CTF](../../banner.png)

# haxxor

We are given an encrypted string:
```
Encrypted string : 0x2-0x19-0x14-0x1d-0x1d-0x2a-0x9-0x61-0x3-0x62-0x15-0xe-0x60-0x5-0xe-0x19-0x4-0x19-0x2c
```

The title gives us the hint to use XOR. Lazy as I am i searched online for another solver and edited it to my pleasure:

```py
##edited: https://ctftime.org/writeup/9230

cipher = '0219141d1d2a09610362150e60050e1904192c'.decode('hex')

for i in range(0x00,0xff):
    result = ''
    for j in cipher:
        result += chr(i^ord(j))
    if 'SHELL{' in result:
        print 'flag :', result
```

That's enough to calc the flag:
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ python2.7 ./haxxor.py
flag : SHELL{X0R3D_1T_HUH}

```
