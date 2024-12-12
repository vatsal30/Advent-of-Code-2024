from collections import deque, defaultdict

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def visit_2(point, data, visited):
  rows, cols = len(data), len(data[0])
  queue = deque([point])
  x, y = point
  visited[x][y] = True
  c = data[x][y]
  area = 0
  side_lookup = defaultdict(set)
  while queue:
    px, py = queue.popleft()
    area += 1
    for dx, dy in DIRECTIONS:
      x1, y1 = px + dx, py + dy
      if 0 <= x1 < rows and 0 <= y1 < cols and not visited[x1][y1] and data[x1][y1] == c:
        visited[x1][y1] = True
        queue.append((x1, y1))
      elif not (0 <= x1 < rows and 0 <= y1 < cols) or data[x1][y1] != c:
        side_lookup[(dx, dy, x1 if dx != 0 else y1)].add((x1 if dx == 0 else y1))
  
  sides = 0
  for _, side_items in side_lookup.items():
    sides += 1
    sorted_side_items = sorted(side_items)
    for i in range(1, len(sorted_side_items)):
      if sorted_side_items[i] - sorted_side_items[i-1] != 1:
        sides += 1
  return area, sides

def part_2(data):
  rows, cols = len(data), len(data[0])
  visited = [[False] * cols for _ in range(rows)]
  ans = 0
  for i in range(rows):
    for j in range(cols):
      if not visited[i][j]:
        area, sides = visit_2((i, j), data, visited)
        ans += area * sides
  return ans

def visit_1(point, data, visited):
  rows, cols = len(data), len(data[0])
  queue = deque([point])
  x, y = point
  visited[x][y] = True
  c = data[x][y]
  area = 0
  perimeter = 0
  while queue:
    px, py = queue.popleft()
    area += 1
    for direction in DIRECTIONS:
      dx, dy = direction
      x1, y1 = px + dx, py + dy
      if 0 <= x1 < rows and 0 <= y1 < cols and not visited[x1][y1] and data[x1][y1] == c:
        visited[x1][y1] = True
        queue.append((x1, y1))
      elif not (0 <= x1 < rows and 0 <= y1 < cols) or data[x1][y1] != c: 
        perimeter += 1
  return area, perimeter


def part_1(data):
  rows, cols = len(data), len(data[0])
  visited = [[False] * cols for _ in range(rows)]
  ans = 0
  for i in range(rows):
    for j in range(cols):
      if not visited[i][j]:
        area, perimeter = visit_1((i, j), data, visited)
        ans += area * perimeter
  return ans

data = []
with open('./inputs.txt', 'r') as f:
  for line in f:
    data.append(list(line.strip()))

ans1 = part_1(data)
ans2 = part_2(data)
print(f"Part 1 solution {ans1}")
print(f"Part 2 solution {ans2}")