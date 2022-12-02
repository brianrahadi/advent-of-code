file = [x for x in open("input.txt").read().strip().split('\n')]

ans = 0
# enemy rps abc
# me rps xyz

def who_win(enemy, me):
  if enemy == 'A':
    if me == 'X':
      return 3
    elif me == 'Y':
      return 6
    else:
      return 0
  elif enemy == 'B':
    if me == 'X':
      return 0
    elif me == 'Y':
      return 3
    else:
      return 6
  else:
    if me == 'X':
      return 6
    elif me == 'Y':
      return 0
    else:
      return 3


score = 0

for line in file:
  if line[2] == 'X':
    score += 1
  elif line[2] == 'Y':
    score += 2
  else: 
    score += 3
  score += who_win(line[0], line[2])

print(score)