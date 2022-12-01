file = [x for x in open("input.txt").read().strip().split('\n')]

maxe = 0
arr = []
current = 0

for str in file:
  if str == '':
    current = 0
  else:
    current += int(str)
    maxe = max(maxe, current)
    arr.append(current)

arr.sort()

ans2 = 0
for i in range(len(arr) - 1, len(arr) - 4, -1):
  ans2 += arr[i]

print(maxe) # part 1 answer
print(ans2) # part 2 answer

