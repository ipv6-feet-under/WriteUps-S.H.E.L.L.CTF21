![S.H.E.L.L.CTF](../../banner.png)

# assembly

In this challenge we were given the following assembly code to analyze:
```asm
fun1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    <fun1+28>
	<+20>:	add    DWORD PTR [ebp-0x4],0x7
	<+24>:	add    DWORD PTR [ebp-0x8],0x70
	<+28>:	cmp    DWORD PTR [ebp-0x8],0x227
	<+35>:	jle    <fun1+20>
	<+37>:	mov    eax,DWORD PTR [ebp-0x4]
	<+40>:	leave  
	<+41>:	ret  
```
According to the challenge, the flag gets calculated by:
```
fun1(0x74,0x6f) + fun1(0x62,0x69) 
```
We can reconstruct the assembly algorithm and convert it into python:
```python
#Parameters given from the challenge
param1= "0x74"
param2= "0x6f"
param3= "0x62"
param4= "0x69"

#Parameter conversion to integer
int1= int(param1,16)
int2= int(param2,16)
int3= int(param3,16)
int4= int(param4,16)

#Copy of the assembly function in python
def fun1(p2,p1):
	while p2 < int("0x227",16):
		p1+= int("0x7",16)
		p2+= int("0x70",16)
	return p1

#Perform the addition from the challenge and print the hex value
print(hex(fun1(int1,int2)+fun1(int3,int4)))
```
This script gives us an integer value, that is 0x117.
We can bring that into the flag format and submit our flag:
```
SHELL{0x117}
```
