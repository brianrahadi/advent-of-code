from collections import deque
# credit to r/jonathanpaulson for making me realize I should use BFS instead. (was trying to do a recursion DFS)
file = [x for x in open('input.txt').read().strip().split("\n")]

matrix = []
for line in file:
  matrix.append([char for char in line])

# find start index
for r in range(len(matrix)):
  for c in range(len(matrix[0])):
    if matrix[r][c] == 'S':
      matrix[r][c] = 'a'
      start = (r, c)
    elif matrix[r][c] == 'E':
      matrix[r][c] = 'z'
      end = (r, c)


visited = set()

def shortest_path():
  while Q:
    (row, col), dist = Q.popleft()

    if (row, col) in visited:
      continue

    visited.add((row, col))

    print((row, col), end)
    if (row, col) == end:
      return dist
    
    for x, y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
      dx = row + x
      dy = col + y

      if 0 <= dx <= len(matrix) - 1 and 0 <= dy <= len(matrix[0]) - 1 and (ord(matrix[row][col]) + 1 >= ord(matrix[dx][dy])):
        Q.append(((dx, dy), dist + 1))

  
Q = deque()
Q.append((start, 0))
print(shortest_path())