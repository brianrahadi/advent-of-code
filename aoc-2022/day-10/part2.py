file = [x for x in open('input.txt').read().strip().split("\n")]

cycle = 0
value = 0

string = ""

for line in file:
  words = line.split()

  # perform no matter if noop or addx
  if cycle % 40 in {value, value+1, value+2}: # check if cycle % 40 is equal to one of these 3 values
      string += "#"
  else:
      string += "."
  cycle += 1

  if words[0] == "addx":
    if cycle % 40 in {value, value + 1, value+2}: # check if cycle % 40 is equal to one of these 3 values
      string += "#"
    else:
      string += "."
    value += int(words[1])
    cycle += 1
  
# print result
for i in range(0, len(string), 40):
  print(string[i:i+40])
