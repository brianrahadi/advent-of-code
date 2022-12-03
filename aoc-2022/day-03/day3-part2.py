list = [x for x in open('input.txt').read().strip().split("\n")]

ans = []

for i in range(0, len(list), 3):
  sete = set()
  sack1 = list[i]
  sack2 = list[i+1]
  sack3 = list[i+2]

  sete1 = set(sack1)
  sete2 = set(sack2)
  sete3 = set(sack3)

  # for char in sack3:
  #   if char in sete1 and char in sete2:
  #     ans.append(char)
  #     break

  ans.append(sete1.intersection(sete2).intersection(sete3).pop()) # gg wp


sum = 0
for char in ans:
  if char >= 'A' and char <= 'Z':
    sum += 27 + ord(char) - ord('A')
  else:
    sum += 1 + ord(char) - ord('a')

print(sum)