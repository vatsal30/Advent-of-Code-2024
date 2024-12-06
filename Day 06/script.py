
def part_1(data, pos):
  x, y = pos
  visited = set()
  curr_dir_idx = 0
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  while True:
    point = tuple([x, y])
    d1, d2 = directions[curr_dir_idx]
    x1, y1 = x + d1, y + d2
    if x1 >= len(data) or x1 < 0 or y1 >= len(data[0]) or y < 0:
      break
    if data[x1][y1] == '#':
      curr_dir_idx = (curr_dir_idx + 1) % len(directions)
    else:
      x, y = x1, y1
      visited.add(point) 
  return visited, len(visited)

def is_cycle(data, pos):
  visited = set()
  curr_dir_idx = 0
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  x, y = pos
  while True:
    point = tuple([x, y, curr_dir_idx])
    if point in visited:
      return True
    direction = directions[curr_dir_idx]
    x1, y1 = x + direction[0], y + direction[1]
    if x1 > len(data) - 1 or x1 < 0 or y1 <0 or y1> len(data[0])-1:
      return False
    if data[x1][y1] == '#':
      curr_dir_idx = (curr_dir_idx + 1) % len(directions)
    else:
      x, y = x1, y1
      visited.add(point)

def part_2(data, pos, visited):
  cycles = 0
  for x in range(len(data)):
    for y in range(len(data[0])):
      if data[x][y] == '.' and tuple([x, y]) in visited:
        data[x][y] = '#'
        cycles += is_cycle(data, pos)
        data[x][y] = '.'
  return cycles

data = []
guard_pos = []
with open('./inputs.txt', 'r') as f:
    idx = 0
    for line in f:
      if '^' in line:
        guard_pos = [idx, line.index('^')]
      data.append(list(line.strip()))
      idx+=1

visited, result = part_1(data, guard_pos)
print(f"Part 1: {result}")
print(f"Part 2: {part_2(data, guard_pos, visited)}")