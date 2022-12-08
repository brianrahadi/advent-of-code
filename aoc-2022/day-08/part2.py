file = [x for x in open('input.txt').read().strip().split('\n')]

matrix = []
for line in file:
  matrix.append(list(map(int, line)))

def scenicValue(row, col):
  right = 0
  # go right
  for c in range(col + 1, len(matrix[0])):
    if matrix[row][col] > matrix[row][c]:
      right += 1
    else:
      right += 1
      break

  left = 0
  for c in range(col - 1, -1, -1):
    if matrix[row][col] > matrix[row][c]:
      left += 1
    else:
      left += 1
      break

  bot = 0
  for r in range(row + 1, len(matrix)):
    if matrix[row][col] > matrix[r][col]:
      bot += 1
    else:
      bot += 1
      break
  
  top = 0
  for r in range(row - 1, -1, -1):
    if matrix[row][col] > matrix[r][col]:
      top += 1
    else:
      top += 1
      break
  
  return right * left * bot * top

maxe = float("-inf")
for r in range(len(matrix)):
  for c in range(len(matrix[0])):
    maxe = max(maxe, scenicValue(r, c))


print(maxe)

