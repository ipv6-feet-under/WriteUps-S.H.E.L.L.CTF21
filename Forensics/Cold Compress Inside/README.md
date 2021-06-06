![S.H.E.L.L.CTF](../../banner.png)

# Cold Compress Inside

We are given [this image](COLD_COMPRESS.jpeg).
Running `file` on it quickly tells us it's a PNG even though it has .jpeg extension.

Now we can use [this really nice tool kit from github](https://github.com/DominicBreuker/stego-toolkit) and run `check_png.sh` on it.
In the `zsteg` part of the output we find the flag:

![flag.png](flag.png)
