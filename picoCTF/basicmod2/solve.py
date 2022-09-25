import string

def modInverse(x, m):
  for i in range(0, m+1):
    if (x * i) % m == 1:
      return i

buffer = open("./message.txt", "r").read().split(" ")
# values = [int(item) for item in buffer]
res = []
x = 0

values = []

for val in buffer:
  values.append(modInverse(int(val), 41))

keys = dict(zip(range(1, 27), string.ascii_uppercase))

for i in range(27, 37):
  keys[i] = x
  x += 1

keys[37] = '_'

for val in values:
  res.append(int(val) % 41)

hasil = []

for val in res:
  for k, v in keys.items():
    if val == k:
      hasil.append(v)

print(*hasil, sep="")
# print(res)