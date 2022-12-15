import math
file = [x for x in open("sample.txt").read().strip().split("\n")]

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

n_checked = 0

### CODE FROM r/jonathanpaulson
for s in setS:
  (sx, sy, d) = S
  for dx in range(d+2):
    dy = (d+1) - dx
    for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
      n_checked += 1
      x = sx+(dx*signx)
      y = sy+(dy*signy)
      if not(0<=x<=4000000 and 0<=y<=4000000):
          continue
      assert abs(x-sx)+abs(y-sy)==d+1

      if not distress_exists(x,y,S):
          print(x*4000000 + y)
          exit(0)

print(counter)

# for (sx,sy,d) in S:
#     # check all points that are d+1 away from (sx,sy)
#     for dx in range(d+2):
#         dy = (d+1)-dx
#         for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
#             n_checked += 1
#             x = sx+(dx*signx)
#             y = sy+(dy*signy)
#             if not(0<=x<=4000000 and 0<=y<=4000000):
#                 continue
#             assert abs(x-sx)+abs(y-sy)==d+1
#             if valid(x,y,S) and (not found_p2):
#                 print(x*4000000 + y)
#                 found_p2 = True