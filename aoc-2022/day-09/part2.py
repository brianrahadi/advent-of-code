file = [x for x in open('input.txt').read().strip().split('\n')]

pointH = [0, 0] # distance between H and T
pointTs = [[0, 0] for _ in range(9)]
pointSet = set()

pointSet.add(tuple(pointTs[8]))

## FINALLY!
def move(H, T):
  dist = [H[0] - T[0], H[1] - T[1]]
  if abs(dist[0]) == 2:
    T[0] += 1 if dist[0] == 2 else -1
    if dist[1] >= 1:
      T[1] += 1
    elif dist[1] <= -1:
      T[1] -= 1
  elif abs(dist[1]) == 2:
    T[1] += 1 if dist[1] == 2 else -1
    if dist[0] >= 1:
      T[0] += 1
    elif dist[0] <= -1:
      T[0] -= 1
    

for line in file:
  way, amt = line.split()
  amt = int(amt)
  for _ in range(amt):
    if way == 'R':
      pointH[0] += 1
    elif way == 'U':
      pointH[1] += 1
    elif way == 'L':
      pointH[0] -= 1
    elif way == 'D':
      pointH[1] -= 1
    move(pointH, pointTs[0])
    
    for i in range(8):
      move(pointTs[i], pointTs[i+1])
    pointSet.add(tuple(pointTs[8]))

print(len(pointSet)) 
    


