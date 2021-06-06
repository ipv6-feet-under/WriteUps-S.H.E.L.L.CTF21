![S.H.E.L.L.CTF](../../banner.png)

# Easy-RSA

We are given some parameters of the RSA:
```
n = 1763350599372172240188600248087473321738860115540927328389207609428163138985769311
e = 65537
c = 334752481114211949024977428768859353103048624289808755223333038405651136629435
```
Just by using the awesome RsaCtfTool (https://github.com/sourcekris/RsaCtfTool or https://github.com/Headorteil/RsaCtfTool) we get the flag:

```bash
┌──(kali㉿kali)-[~/Desktop/RsaCtfTool/RsaCtfTool]
└─$ python3 ./RsaCtfTool.py -n 1763350599372172240188600248087473321738860115540927328389207609428163138985769311 -e 65537 --uncipher 33475248111421194902497742876885935310304862428980875522333303840565113662943528
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmpnodtpx0t.
[*] Performing smallq attack on /tmp/tmpnodtpx0t.
[*] Performing mersenne_primes attack on /tmp/tmpnodtpx0t.
 24%|████████████████████████████████                                                                                                        | 12/51 [00:00<00:00, 399457.52it/s]
[*] Performing system_primes_gcd attack on /tmp/tmpnodtpx0t.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7007/7007 [00:00<00:00, 1625075.37it/s]
[*] Performing fibonacci_gcd attack on /tmp/tmpnodtpx0t.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 340797.21it/s]
[*] Performing factordb attack on /tmp/tmpnodtpx0t.
[*] Attack success with factordb method !

Results for /tmp/tmpnodtpx0t:

Unciphered data :
HEX : 0x00000000007368656c6c7b737769746368696e5f746f5f6173796d6d65747269637d
INT (big endian) : 3111388068276188662361997958100924356274395167698926770307665056326525
INT (little endian) : 3716857967501616239523840250653395077772235796196542527851123201402003116282347520
STR : b'\x00\x00\x00\x00\x00shell{switchin_to_asymmetric}'
```
