![S.H.E.L.L.CTF](../../banner.png)

# keygen

In this challenge we were given the following python script:
```python
def checkends(password):
    end_status = 0
    if password[:6] == "SHELL{":
        end_status = 1
    if password[28] == "}":
        end_status = 1
    return end_status
def checkmiddle1(password):
    middle1_status = 0
    if password[27] == "1"  and password[17] == "4" and password[8] == "n" and password[23] == "y" and password[10] == "0":
        middle1_status = 1
    if password[11] == "n" and password[12] == "z" and password[13] == "a" and password[21] == "g" and password[15] == "u":
        middle1_status = 1
    if password[16] == "r"and password[7] == "3" :
        middle1_status = 1
    return middle1_status
def checkmiddle2(password):
    middle2_status = 0
    if password[18] == "_" and password[25] == "5" and password[20] == "4" and password[14] == "k" and password[22] == "3" and password[9] == "b"  and password[24] ==  "0":
        middle2_status = 1
    if  password[19] == "k" and password[26] == "h" and password[6] == "s" :
        middle2_status = 1
    return middle2_status
# driver code

a = input("enter your flag:")
if checkends(a) == 1 and checkmiddle1(a) == 1 and checkmiddle2(a) == 1:
    print("congrats thats the flag.")
else:
    print("Wrong flag.")
```
We can see, that there are 3 functions, that check, if the submitted flag is valid. looking into the funcitons we see alot of passes that look like this:
```
if password[27] == "1"  and password[17] == "4" and password[8] == "n" and password[23] == "y" and password[10] == "0":
```
Here we can see, that at the 27th position of the array is a `1`, at the 17th position a `4` etc.

This way we can reconstruct the complete flag:
```
SHELL{s3nb0nzakur4_k4g3y05h1}
```
