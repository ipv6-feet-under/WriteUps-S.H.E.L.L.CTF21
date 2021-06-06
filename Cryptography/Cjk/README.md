![S.H.E.L.L.CTF](../../banner.png)

# CJK

We are given an png with symbols to find a PIN:

![pin](images/pin.png)

The title CJK gives us a hint to find the symbols in unicode: https://en.wikipedia.org/wiki/CJK_characters

Now we can search for a specific cutout for CJK-Symbols in unicode and search around that area: https://www.unicode.org/charts/PDF/U3000.pdf

![symbols](images/symbols_in_table.png)

Now we can sum the values:

![calc](images/calc.PNG)

This number is the PIN we can use for the flag: SHELL{9053}
