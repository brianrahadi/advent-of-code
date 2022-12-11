file = [x for x in open('input.txt').read().strip().split("\n")]

monkeys = []
ops = []
divs = []
trues = []
falses = []
inspects = [0] * 10

counter = 0
op = []
monkey = []

for line in file:
  counter += 1
  words = line.split()
  if counter == 2:
    for i in range(2, len(words)):
      monkey.append(int(words[i].replace(',', '')))
  elif counter == 3:
    op.append(words[len(words) - 2])
    if words[len(words) - 1] == "old":
      op.append((words[len(words) - 1]))
    else:
      op.append(int(words[len(words) - 1]))
    ops.append(op)
    op = []
    # print(3, words)
  elif counter == 4:
    divs.append(int(words[len(words) - 1]))
  elif counter == 5:
    trues.append(int(words[len(words) - 1]))
  elif counter == 6:
    falses.append(int(words[len(words) - 1]))
  elif line == "":
    counter = 0
    monkeys.append(monkey)
    monkey = []

monkeys.append(monkey)

rounds = 10000
lcm = 1
for div in divs:
  lcm *= div # key in solving part 2 credit to r/jonathanpaulson from r/adventofcode for the logic!
  
for r in range(rounds):
  for i in range(len(monkeys)):
    for j in range(len(monkeys[i])):
      inspects[i] += 1
      if len(monkeys[i]) == 0:
        continue
      item = monkeys[i].pop(0)
      if ops[i][0] == '*':
        if ops[i][1] == "old":
          item *= item
        else:
          item *= ops[i][1]
      else:
        if ops[i][1] == "old":
          item += item
        else:
          item += ops[i][1]
      item %= lcm
      if item % divs[i] == 0:
        monkeys[trues[i]].append(item)
      else:
        monkeys[falses[i]].append(item)


inspects.sort(reverse = True)
monkey_business = inspects[0] * inspects[1]
print(monkey_business)
