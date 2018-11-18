import sys
L = len(sys.argv) - 1

for x in range(L):
  num = int(sys.argv[x + 1])
  if (num % 2 == 0):
    print(num)
