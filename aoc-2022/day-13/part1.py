
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
    exit(1)


sum_index = 0
counter = 1

for i in range(0, len(file), 3):
  arr1 = eval(file[i])
  arr2 = eval(file[i+1])

  ponyo = in_right_order(arr1, arr2)
  sum_index += counter if in_right_order(arr1, arr2) == 1 else 0

  counter += 1

print(sum_index)
