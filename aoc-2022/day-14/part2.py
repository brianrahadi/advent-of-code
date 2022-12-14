## credit https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/14.py

file = [x for x in open('input.txt').read().strip().split("\n")]

arr = []
blocks = set()

for line in file:
  line = line.split(" -> ")
  paths = []
  prev = None
  for coord in line:
    (x, y) = tuple(map(int, coord.split(',')))

    if prev is not None:
      delta_x = x - prev[0]
      delta_y = y - prev[1]
      length = max(abs(delta_x), abs(delta_y))

      if delta_x != 0:
        for i in range(length + 1):
          block_x = prev[0] + i * (-1 if delta_x < 0 else 1)
          blocks.add((block_x, y))
      else:
        for i in range(length + 1):
          block_y = prev[1] + i * (-1 if delta_y < 0 else 1)
          blocks.add((x, block_y))

    prev = (x, y)


    paths.append((x, y))
  arr.append(paths)


floor = max(block[1] for block in blocks) + 2

leftest = min(block[0] for block in blocks) - 2000
rightest = max(block[0] for block in blocks) + 2000

for x in range(leftest, rightest):
  blocks.add((x, floor))

for units in range(1000000):
  block = [500, 0]
  while True:    
    ## keep going downnn
    if (block[0], block[1]+1) not in blocks:
      block[1] += 1
    elif (block[0] - 1, block[1] + 1) not in blocks:
      block[0] -= 1
      block[1] += 1
    elif (block[0] + 1, block[1] + 1) not in blocks:
      block[0] += 1
      block[1] += 1
    else:
      break

  if block == [500, 0]:
    print(units + 1)
    exit(0)
  blocks.add(tuple(block))