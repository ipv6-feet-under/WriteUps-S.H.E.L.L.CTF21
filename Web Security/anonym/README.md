![S.H.E.L.L.CTF](../../banner.png)

# anonym
### Anonymous are back and they really hate robots.

The description already hints us to the robot.txt so let's have a look at it:
http://3.142.122.1:8887/robots.txt
```
User-agent: *
Disallow: /yfhdgvs.txt

```

The robots.txt doesn't want search engines to list the `yfhdgvs.txt` so let's have a look at that as well:
http://3.142.122.1:8887/yfhdgvs.txt

```
SHELL{n0_ro80t5_4llow3d_50886509749a98ef14ec2bc45c57958e}
```
