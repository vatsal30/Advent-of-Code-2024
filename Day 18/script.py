from collections import deque, defaultdict

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
data = []
# memory_space = [[None for _ in range(70)] for _ in range(70)]

with open('./inputs.txt', 'r') as f:
  for line in f:
    data.append(list(map(lambda x: int(x), line.strip().split(','))))

def visitor(point, grid, visited):
  queue = deque([(point, 0)])
  x, y = point
  visited[x][y] = True
  goal = (70, 70)
  while queue:
    (px, py), steps = queue.popleft()
    if (px, py) == goal:
      return steps
    for direction in DIRECTIONS:
      dx, dy = direction
      x1, y1 = px + dx, py + dy
      if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
        if grid[x1][y1] == '.' and not visited[x1][y1]:
          visited[x1][y1] = True
          queue.append(((x1, y1), steps + 1))
  return -1

def part_1(data):
  memory_space = [['.' for _ in range(71)] for _ in range(71)]
  visited = [[False] * 71 for _ in range(71)]
  for x, y in data[:1024]:
    memory_space[x][y] = '#'
  ans = visitor((0, 0), memory_space, visited)
  return ans

def part_2(data):
  memory_space = [['.' for _ in range(71)] for _ in range(71)]
  
  for x, y in data[:1024]:
    memory_space[x][y] = '#'
  for x, y in data[1024:]:
    memory_space[x][y] = '#'
    visited = [[False] * 71 for _ in range(71)]
    ans = visitor((0, 0), memory_space, visited)
    if ans == -1:
      return x,y
  return ans

print(part_1(data))
print(part_2(data))
  