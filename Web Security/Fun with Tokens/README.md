![S.H.E.L.L.CTF](../../banner.png)

# Fun with Tokens

Visiting the provided website we see some interesting thing:
There are two links:

http://3.142.122.1:9334/login
http://3.142.122.1:9334/adminNames

And comments in the Source:
```
<!-- /admin is where the fun's at XD -->
<!--The secret you seek is in the environment-->
```

Admin names sounds interesting so let's check that first:
![curl](curl.png)

There is actually a redirect to a getFile.php interesting.
Opening http://3.142.122.1:9334/getFile?file=admins in a browser provides us a list with admin names:

```
0xd4127c3c
din_djarin11
```

This already looks a lot like there might be LFI possible. We have the hint that there is some secret in the environment so let's try to pull the .env file using the getFile.php:

http://3.142.122.1:9334/getFile?file=.env
```
No such file or directory: /app/public/.env
```

Okay but maybe in the /app directory?

http://3.142.122.1:9334/getFile?file=../.env

```
secret=G00D_s0ld13rs_k33p_s3cret5
```
Sweet! Unfortunately this is not our flag so we have to search further. Let's have at /admin as the hint said that's where the fun is supposed to be.

http://3.142.122.1:9334/admin
```
{"success":false,"message":"Maybe send the token via Headers ... for Authorization?"}
```

This is some kind of API but we are not authorized. It seems like we need a token, we already have a secret_key which is used to sign tokens so this will propably be our attack vector.
We don't have any cookies/tokens yet so let's check our /login page.

Sending `test:test` in the form of the /login page responses with a token in the header:
![header_token](header_token.png)

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImdyZmciLCJwYXNzd29yZCI6ImdyZmciLCJhZG1pbiI6InNueWZyIiwiaWF0IjoxNjIyOTc3MjI4fQ.nMCBVHmSiRpfV_nMnDqlTFLemUiIHePimxCP8UqPU9c
```
Let's decrypt it using https://jwt.io
![jwt_io.png](jwt_io.png)

We can see username and password, however they are not what we sent.. `test` got translated to `grfg`. Let's send the alphabet to get the subsitution alphabet:

```
abcdefghijklmnopqrstuvwxyz
nopqrstuvwxyzabcdefghijklm
```

We are now able to translate our username and password propably, also we notice that it says `false` inside the admin parameter.
Let's craft our new token using everything we have so far:
```
username: qva_qwneva11 (din_djarin11 translated using our subsitution alphabet)
password: empty we don't have one yet
admin: gehr (translation of true)
signature key: G00D_s0ld13rs_k33p_s3cret5
```

It should look like this:
![crafted_jwt](crafted_jwt.png)

Let's send that token to /admin as our authorization header:
![send_token](send_token.png)

```
FURYY{G0x3af_q0_z4gg3e_4r91ns4506s384q460s0s0p6r9r5sr4n}
```
Translating this with our subsitutin alphabet or sending it as a username and read that token gives us the flag:
```
SHELL{T0k3ns_d0_m4tt3r_4e91af4506f384d460f0f0c6e9e5fe4a}
```