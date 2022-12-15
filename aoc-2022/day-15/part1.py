import math
file = [x for x in open("input.txt").read().strip().split("\n")]

setB = set()
setS = set()
dictSB = dict() # key is sensor, value is closest beacon

def dist(B, S):
  return abs(B[0] - S[0]) + abs(B[1] - S[1])

for line in file:
  line = line.replace("Sensor at ", "").replace(",", "").replace(": closest beacon is at", "").replace("x=", "").replace("y=", "").split()
  
  S = (int(line[0]), int(line[1]))
  B = (int(line[2]), int(line[3]))
  distSB = dist(B, S)
  setS.add((S[0], S[1], distSB))
  setB.add(B)

  dictSB[S] = B
  # print(S, B)

def distress_exists(beacon):
  for s in setS:
    curr_dist = dist(beacon,s)
    if curr_dist <= s[2]:
      return True
    
  return False

beacon_y = 2e6
counter = 0

for x in range(-int(1e7), int(1e7)):
  beacon = (x, beacon_y)
  if beacon not in setB and distress_exists(beacon):
    counter += 1
  

print(counter)

