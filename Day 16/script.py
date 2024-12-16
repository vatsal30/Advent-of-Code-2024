
from heapq import heappush, heappop
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part_2(data, start, end, best_cost):
  pq = []
  heappush(pq, (0, start[0], start[1], 1, []))
  ans = set()
  visited = {}
  while pq:
      cost, x, y, direction, path = heappop(pq)
      if (x, y) == end and cost <= best_cost:
        ans.update(path + [(x, y)])
        continue

      if (x, y, direction) in visited and visited[(x, y, direction)] != cost:
          continue
      visited[(x, y, direction)] = cost
      new_path = path + [(x, y)]

      dx, dy = DIRECTIONS[direction]
      nx, ny = x + dx, y + dy
      if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and data[nx][ny] != '#':
          heappush(pq, (cost + 1, nx, ny, direction, new_path))

      cw_direction = (direction + 1) % 4
      heappush(pq, (cost + 1000, x, y, cw_direction, new_path))

      ccw_direction = (direction - 1) % 4
      heappush(pq, (cost + 1000, x, y, ccw_direction, new_path))
  return ans

def part_1(data, start, end):
  pq = []
  heappush(pq, (0, start[0], start[1], 1))
  visited = set()
  while pq:
      cost, x, y, direction = heappop(pq)
      if (x, y) == end:
          return cost
      if (x, y, direction) in visited:
          continue
      visited.add((x, y, direction))

      dx, dy = DIRECTIONS[direction]
      nx, ny = x + dx, y + dy
      if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and data[nx][ny] != '#':
          heappush(pq, (cost + 1, nx, ny, direction))

      cw_direction = (direction + 1) % 4
      heappush(pq, (cost + 1000, x, y, cw_direction))

      ccw_direction = (direction - 1) % 4
      heappush(pq, (cost + 1000, x, y, ccw_direction))

start = tuple()
end = tuple()
data = []
with open('./inputs.txt', 'r') as f:
  for i, line in enumerate(f):
    data.append(list(line.strip()))
    try:
      idxE = data[i].index('E')
      end = (i, idxE)
    except:
      pass
    try:
      idxS = data[i].index('S')
      start = (i, idxS)
    except:
      pass

lowest_cost = part_1(data, start, end)
print(f"Part 1 Solutions: {lowest_cost}")
ans2 = part_2(data, start, end, lowest_cost)
print(f"Part 2 Solutions: {len(ans2)}")
