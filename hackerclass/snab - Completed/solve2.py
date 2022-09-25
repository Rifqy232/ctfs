#Snab says good job! But you're not done yet
from Cryptodome.Util.number import *
# from secret import FLAG

# flag = FLAG
# halfa = ''.join([flag[i] for i in range (0, len(flag), 2)])
# halfb = ''.join([flag[i] for i in range (1, len(flag), 2)])
# p = bytes_to_long(bytes(halfa, encoding = 'utf-8'))
# q = bytes_to_long(bytes(halfb, encoding = 'utf-8'))
# r = 0

# while (not(isPrime(p) and isPrime(q))):
#   p += 1
#   q += 1
#   r += 1

r = 23728
p = 1995013714358934674788753256494703046979981946405060402188831027417831621430580449
q = 2351073938238335675017307353569618225242960896099574020278868141802745118893116717

pmr = p-r
qmr = q-r

pwords = long_to_bytes(pmr)
qwords = long_to_bytes(qmr)

out = ""
for i in range(len(pwords)):
  out += chr(pwords[i]) + chr(qwords[i])

print(out)