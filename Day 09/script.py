
def part_2(data):
  new_data = []
  cnt = 0
  file = []
  free = []
  pos = 0
  for idx, num in enumerate(data):
    if idx % 2 == 0:
      file.append((pos, num, cnt))
      new_data.extend([cnt] * num)
      cnt += 1
      pos += num
    else:
      free.append((pos, num))
      new_data.extend(['.'] * num)
      pos += num
  print(new_data)
  print(file)
  print(free)
  
  for file_idx, file_size, file_id in reversed(file):
    for space_pos, (space_idx, space_size) in enumerate(free):
      if space_idx < file_idx  and space_size >= file_size:
        for i in range(file_size):
          new_data[file_idx + i] = '.'
          new_data[space_idx + i] = file_id
        free[space_pos] = (space_idx + file_size, space_size - file_size)
        break
  
  checksum = 0
  cnt = 0
  for i in new_data:
      if i == '.':
        cnt += 1
        continue
      checksum += cnt * int(i)
      cnt += 1
  return checksum


def part_1(data):
    new_data = []
    cnt = 0
    for idx, num in enumerate(data):
      if idx % 2 == 0:
        new_data.extend([cnt] * num)
        cnt += 1
      else:
         new_data.extend(['.'] * num)
    ptr = new_data.index('.')
    ptr2 = len(new_data) - 1
    
    while ptr2 > ptr:
      new_data[ptr2], new_data[ptr] = new_data[ptr], new_data[ptr2]
      ptr += 1
      ptr2 -= 1
      while new_data[ptr2] == '.':
       ptr2 -= 1
      while new_data[ptr] != '.':
       ptr += 1
    cnt = 0
    checksum = 0
    for i in new_data:
      if i == '.':
        break
      checksum += cnt * int(i)
      cnt += 1
    return checksum

data = []
temp = ''
with open('./inputs.txt', 'r') as f:
    temp = f.read()
    data = list(map(lambda x: int(x), list(temp.strip())))

print(part_1(data))
print(part_2(data))