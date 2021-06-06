![S.H.E.L.L.CTF](../../banner.png)

# Algoric-Shift

In this challenge we were given an encrypted flag:
```
HESL{LRAT5PN51010T_CNPH1R}3
```

And a python script that includes the encryption algorithm:
```python
text = 'flag{...}'

key = [3,1,2]

li0 = []
li1 = []
li2 = []
for i in range(0,len(text)):
    if i % 3 == 0:
        li0.append(text[i])
    elif (i - 1) % 3 == 0:
        li1.append(text[i])
    elif (i - 2) % 3 == 0:
        li2.append(text[i])
li = []
for i in range(len(li1)): 
    li.append(li1[i]) 
    li.append(li2[i])
    li.append(li0[i])

# print(li)
print("The ciphered text is :")
ciphered_txt = (''.join(li))
print(ciphered_txt)
```
To solve this challenge we changed the `text` variable to `SHELL{ABCDEFGHIJKLMNOPQRST}`.

This is the whole alphabet, that is used by the flag we received.

We can now look at the output the script gives, when we execute it with our changed `text`variable:
```
HESL{LBCAEFDHIGKLJNOMQRPT}S
```
Because we know the flag begins with `SHELL{` we can take that part for granted.

For the rest of the flag we simply need to overlay the three flags we now have.

```
HESL{LRAT5PN51010T_CNPH1R}3
SHELL{ABCDEFGHIJKLMNOPQRST}
HESL{LBCAEFDHIGKLJNOMQRPT}S
```

We can now see how the encryption changes the position of the letters and can reconstruct the flag:
```
SHELL{TRAN5P051T10N_C1PH3R}
```
