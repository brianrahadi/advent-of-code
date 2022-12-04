list = [x for x in open('input.txt').read().strip().split("\n")]

def inside(half1, half2):
  half1_1, half1_2 = half1.split('-')
  half2_1, half2_2 = half2.split('-')
  

  if int(half1_1) <= int(half2_1) and int(half1_2) >= int(half2_2):
    return True
  return False

counter = 0

for line in list:
  half1, half2 = line.split(',')
  if inside(half1, half2) or inside(half2, half1):
    counter += 1

print(counter)
