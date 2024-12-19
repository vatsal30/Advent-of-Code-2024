
designs = []
patterns = []

with open('./inputs.txt', 'r') as f:
  for idx, line in enumerate(f):
    if idx == 0:
      patterns = line.strip().split(', ')
      continue
    if idx == 1:
      continue
    designs.append(line.strip())

def solve(design, part2 = False):
  matches = [0] * (len(design) + 1)
  matches[0] = 1
  for i in range(1, len(design) + 1):
    for pattern in patterns:
      if i >= len(pattern) and design[i - len(pattern):i] == pattern and matches[i-len(pattern)]:
        matches[i] += matches[i - len(pattern)]
        if not part2:
          break
  return matches[-1]

def part_1(designs):
  ans = 0
  for design in designs:
    ans += solve(design)
  return ans

def part_2(designs):
  ans = 0
  for design in designs:
    ans += solve(design, True)
  return ans

print(f"Part 1 solution: {part_1(designs)}")
print(f"Part 2 solution: {part_2(designs)}")
