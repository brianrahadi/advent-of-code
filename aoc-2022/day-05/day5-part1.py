file = [x for x in open("./input.txt").read().strip().split('\n')]

counter = 0
stacks = []
stacks.append([])

for _ in range(1, len(file[1]), 4):
    stacks.append([])

for line in file:
    counter += 1
    index = 0
    if line[1] == '1':
        break
    for i in range(1, len(line), 4):
        index += 1
        if line[i] != ' ' and line[i] != '-':
            stacks[index].append(line[i])

for i in range(counter+1, len(file)):
    amt, from_, to = list(map(int, file[i].replace("move ", "").replace("from ", "").replace("to ", "").split()))
    for _ in range(amt):
        stacks[to].insert(0, stacks[from_].pop(0))

str = ""
for i in range(1, len(stacks)):
    str += stacks[i][0]
print(str)
