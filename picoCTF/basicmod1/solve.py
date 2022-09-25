import string

buffer = open("./message.txt", "r").read().split(" ")
# values = [int(item) for item in buffer]
res = []
x = 0

keys = dict(zip(range(0, 26), string.ascii_uppercase))

for i in range(26, 36):
  keys[i] = x
  x += 1

keys[36] = '_'

for val in buffer:
  res.append(int(val) % 37)

hasil = []

for val in res:
  for k, v in keys.items():
    if val == k:
      hasil.append(v)

print(*hasil, sep="")