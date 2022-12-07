file = [x for x in open("input.txt").read().strip().split('\n')]

charSet = set()
l = 0

str = file[0]

for r in range(len(str)):
  while str[r] in charSet:
    charSet.remove(str[l])
    l += 1
  charSet.add(str[r])
  if len(charSet) == 14:
    print(r+1)
    break