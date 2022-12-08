file = [x for x in open('input.txt').read().strip().split('\n')]

matrix = []
for line in file:
  matrix.append(list(map(int, line)))

boolMat = [[False for _col in range(len(matrix[0])) ] for _row in range(len(matrix))]

# visible from bottom
mini = float('-inf')
for c in range(0, len(matrix[0])):
  mini = float('-inf')
  for r in range(len(matrix) - 1, -1, -1):
    if matrix[r][c] > mini:
      boolMat[r][c] = True
      mini = matrix[r][c]

# visible from top
mini = float('-inf')
for c in range(0, len(matrix[0])):
  mini = float('-inf')
  for r in range(0, len(matrix)):
    if matrix[r][c] > mini:
      boolMat[r][c] = True
      mini = matrix[r][c]

# visible from left
for r in range(0, len(matrix)):
  mini = float('-inf')
  for c in range(0, len(matrix[0])):
    if matrix[r][c] > mini:
      boolMat[r][c] = True
      mini = matrix[r][c]

# visible from right
for r in range(0, len(matrix)):
  mini = float('-inf')
  for c in range(len(matrix[0]) - 1, -1, -1):
    if matrix[r][c] > mini:
      boolMat[r][c] = True
      mini = matrix[r][c]

ans = 0
for r in range(len(boolMat)):
  ans += boolMat[r].count(True)

print(ans)

