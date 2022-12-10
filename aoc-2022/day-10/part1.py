file = [x for x in open('input.txt').read().strip().split("\n")]

cycle = 1
value = 1

answer = 0

for line in file:
  words = line.split()
  if words[0] == "noop":
    cycle += 1
  else:
    cycle += 1
    if cycle % 40 == 20:
      answer += cycle * value
    value += int(words[1])
    cycle += 1
  if cycle % 40 == 20:
    answer += cycle * value


print(answer)
