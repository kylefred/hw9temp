import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
L = y - x + 1

sum = 0

for j in range(L):
  sum += (j + x)**2

print(sum)
