import hashlib

str2hash = "lollipops"
res = hashlib.md5(str2hash.encode())

print(res.hexdigest())