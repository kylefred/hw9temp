import sys
L = len(sys.argv) - 1

myList = [1, 6, 9, 8, 14]

for x in range(L):
  num = int(sys.argv[x + 1])
  myList.append(num)

print(myList)
print(len(myList))
myList.sort()
print(myList)
