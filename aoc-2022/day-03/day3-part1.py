list = [x for x in open('input.txt').read().strip().split("\n")]

ans = []

for line in list:
  half1 = line[0:(len(line)//2)]
  half2 = line[len(line)//2:len(line)]
  sete = set(half1)
  sete2 = set(half2)

  # for char in half2:
  #   if char in sete:
  #     ans.append(char)
  #     break

  ans.append(sete.intersection(sete2).pop())

sum = 0
for char in ans:
  if char >= 'A' and char <= 'Z':
    sum += 27 + ord(char) - ord('A')
  else:
    sum += 1 + ord(char) - ord('a')

print(sum)