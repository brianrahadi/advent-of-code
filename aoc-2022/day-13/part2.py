
from functools import cmp_to_key


file = [x for x in open('input.txt').read().strip().split("\n")]

def in_right_order(el1, el2):
  if isinstance(el1, int) and isinstance(el2, int):
    if el1 < el2:
      return 1
    elif el1 == el2:
      return 0
    else:
      return -1

  elif isinstance(el1, list) and isinstance(el2, list):
    leng = min(len(el1), len(el2))
    for i in range(leng):
      order = in_right_order(el1[i], el2[i])
      if order == 0:
        continue
      return order
    
    if len(el1) < len(el2):
      return 1
    elif len(el1) == len(el2):
      return 0
    else:
      return -1
    
  elif isinstance(el1, int) and isinstance(el2, list):
    return in_right_order(el2, el1) * -1

  elif isinstance(el1, list) and isinstance(el2, int):
    return in_right_order(el1, [el2])
  
  else:
    print("ERROR!")


sum_index = 0
counter = 1

arr = []
arr.append([[2]])
arr.append([[6]])
for i in range(0, len(file), 3):
  arr.append(eval(file[i]))
  arr.append(eval(file[i+1]))

# credit to r/jonathanpaulson for the cmp_to_key idea for sorting the array
arr = sorted(arr, key=cmp_to_key(lambda a, b: -in_right_order(a, b)))  

ans = 1

# iterate through the array with index, value
for index, el in enumerate(arr):
  if el == [[2]] or el == [[6]]:
    ans *= index+1

print(ans)