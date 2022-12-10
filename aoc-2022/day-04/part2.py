list = [x for x in open('input.txt').read().strip().split("\n")]

def overlap(half1, half2):
  half1_1, half1_2 = half1.split('-')
  half2_1, half2_2 = half2.split('-')
  half1_1 = int(half1_1)
  half1_2 = int(half1_2)
  half2_1 = int(half2_1)
  half2_2 = int(half2_2)

  sete = set()
  for num in range(half1_1, half1_2+1):
    sete.add(num)
  
  if half2_1 in sete or half2_2 in sete:
    return True
  return False

counter = 0

for line in list:
  half1, half2 = line.split(',')
  if overlap(half1, half2) or overlap(half2, half1):
    counter += 1

print(counter)
