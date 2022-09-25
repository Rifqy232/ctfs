text = open('./message.txt', "r").read()
res = [word for word in text]
# res.append(text)

counter = 2
for i in range(0, len(res)):
  if i == counter:
    res[counter-2], res[counter-1], res[counter] = res[counter], res[counter-2], res[counter-1]
    counter += 3

print(*res, sep="")