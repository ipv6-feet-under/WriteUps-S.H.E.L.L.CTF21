![S.H.E.L.L.CTF](../../banner.png)

# Bruteforce RSA

We are given some information:
- The flag format:
```
Flag Format : shellctf{}
```
- A python script:
```py
from Crypto.Util.number import bytes_to_long,inverse,getPrime,long_to_bytes
from secret import message
import json

p = getPrime(128)
q = getPrime(128)

n = p * q
e = 65537 

enc = pow(bytes_to_long(message.encode()),e,n)
print("Encrypted Flag is {}".format(enc))

open('./values.json','w').write(json.dumps({"e":e,"n":n,"enc_msg":enc}))
```
- And a values.json:
```json
{"e": 65537, "n": 105340920728399121621249827556031721254229602066119262228636988097856120194803, "enc_msg": 36189757403806675821644824080265645760864433613971142663156046962681317223254}
```
As this are only small primes and enough information of the paramater it's enough to feed the awesome RsaCtfTool (https://github.com/sourcekris/RsaCtfTool or https://github.com/Headorteil/RsaCtfTool):
```bash
┌──(kali㉿kali)-[~/Desktop/RsaCtfTool/RsaCtfTool]
└─$ python3 RsaCtfTool.py -n 105340920728399121621249827556031721254229602066119262228636988097856120194803 -e 65537 --uncipher 36189757403806675821644824080265645760864433613971142663156046962681317223254
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmpr2865b44.
[*] Performing smallq attack on /tmp/tmpr2865b44.
[*] Performing mersenne_primes attack on /tmp/tmpr2865b44.
 24%|████████████████████████████████                                                                                                        | 12/51 [00:00<00:00, 390167.81it/s]
[*] Performing system_primes_gcd attack on /tmp/tmpr2865b44.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7007/7007 [00:00<00:00, 1500688.73it/s]
[*] Performing fibonacci_gcd attack on /tmp/tmpr2865b44.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 344107.96it/s]
[*] Performing factordb attack on /tmp/tmpr2865b44.
[*] Attack success with factordb method !

Results for /tmp/tmpr2865b44:

Unciphered data :
HEX : 0x0000000000007368656c6c6374667b6b33795f73317a655f6d4074746572247d
INT (big endian) : 185453180567955987067286742617490330426585681406450523077485693
INT (little endian) : 56603502101542516885309888740153031607828169274635448325113252619392540213248
STR : b'\x00\x00\x00\x00\x00\x00shellctf{k3y_s1ze_m@tter$}'
```
