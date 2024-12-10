DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def checker(curr, point, data, visited):
  x, y = point
  ans = 0
  for direction in DIRECTIONS:
    dx, dy = direction
    x1, y1 = x + dx, y + dy
    if 0 <= x1 < len(data) and 0 <= y1 < len(data[0]) and data[x1][y1] == curr:
      if curr == 9:
        ans += 1
        visited.add((x1, y1))
        continue
      ans += checker(curr + 1, (x1, y1), data, visited)
  return ans

def get_all_trail_heads(data):
  trail_heads = []
  for i in range(len(data)):
    for j in range(len(data[0])):
      if data[i][j] == 0:
        trail_heads.append((i, j))
  return trail_heads

def part_1_2(data):
  trail_heads = get_all_trail_heads(data)
  ans1 = 0
  ans2 = 0
  for trail_head in trail_heads:
    visited = set()
    # We will get the all possible paths as return from the function
    ans2 += checker(1, trail_head, data, visited)
    ans1 += len(visited)
  return ans1, ans2

data = []
with open('./inputs.txt', 'r') as f:
  for line in f:
    line = list(map(lambda x: int(x), list(line.strip())))
    data.append(line)

ans1, ans2 = part_1_2(data)
print(f"Part 1 solution {ans1}")
print(f"Part 2 solution {ans2}")

