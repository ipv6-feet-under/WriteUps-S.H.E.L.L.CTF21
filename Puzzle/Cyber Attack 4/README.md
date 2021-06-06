![S.H.E.L.L.CTF](../../banner.png)

# Cyber Attack 4


```
We have top secret confidential information from the secret service that there is going to be an all out cyber attack against a country in the future. Long Live our spy who died in between the transmission.

The FBI have found that the following tools will be used in attack on the country.Use this GitHub repo as a starting point for your investigation https://github.com/norias-teind/tools All we ask from you is : The Country of Attack
```

So this is an OSINT challenge and we have to find the county of attack. The other challanges have the same git as origin but are searching for "Country of the attacker", "Name of the attacker" and "Date of the attack". Look in Cyber Attack 1 - 3 to learn about these paths.

The linked Git is a tools repository with the code of the LOIC (Low Orbit Ion Cannon) in it. Looking inside the LOIC directory we find a README.md that's a little bit changed to the original README.md of the LOIC. 
There is a line added that tells us:
```
For code examples check https://realantwohnette.wordpress.com
```
Additionally there is an evil number in the .gitignore file at https://github.com/norias-teind/tools/blob/main/.gitignore

And at the website https://realantwohnette.wordpress.com there is a Cars 2 background on the blog, which is really odd since there is literally nothing else related to that topic at all. So we figured this has to be a hint to something. What sounds easy now took us an eternity, but the background is supposed to be a hint to the "C2 Cipher".

There is also a blog entry in which he says that `c+~X8^Tv5$nhnu}`is a robust password. So let's put these information together in [Cyberchef](https://gchq.github.io/CyberChef/):
![c2](c2.png)

The result is a list of WiFi Networks where the first is `SSID:"Free Wifi Hoograven"`.

Searching google reveals that it is in the Netherlands.

![netherlands](netherlands.png)

SHELL{Netherlands}
