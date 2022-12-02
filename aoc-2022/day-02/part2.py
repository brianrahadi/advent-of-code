file = [x for x in open("input.txt").read().strip().split('\n')]

ans = 0
# enemy rps abc
# me rps xyz

score = 0

for line in file:
  if line[2] == 'X':
    score += 0
    if line[0] == 'A':
      score += 3
    elif line[0] == 'B':
      score += 1
    else:
      score += 2

  elif line[2] == 'Y':
    score += 3
    if line[0] == 'A':
      score += 1
    elif line[0] == 'B':
      score += 2
    else:
      score += 3
  else: 
    score += 6
    if line[0] == 'A':
      score += 2
    elif line[0] == 'B':
      score += 3
    else:
      score += 1

print(score)