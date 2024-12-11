
from collections import Counter

def multiply_by_2024(a):
  return (a << 10) + (a << 9) + (a << 8) + (a << 7) + (a << 6) + (a << 5) + (a << 3)

def blink_single(stone):
	if stone == 0:
		return [1]
	stone_str = str(stone)
	if len(stone_str) % 2 == 0:
		return [int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])]
	else:
		return [multiply_by_2024(stone)]

def part_2(data):
  stones = data
  for _ in range(75):
    temp = Counter()
    for stone, count in stones.items():
      for j in blink_single(stone):
        temp[j] += count
    stones = temp
  return sum(stones.values())

def part_1(data):
  stones = data
  for _ in range(25):
    temp = Counter()
    for stone, count in stones.items():
      for j in blink_single(stone):
        temp[j] += count
    stones = temp
  return sum(stones.values())

data = []
with open('./inputs.txt', 'r') as f:
  for line in f:
    data = Counter(map(lambda x: int(x), line.strip().split(' ')))

ans1 = part_1(data)
ans2 = part_2(data)
print(f"Part 1 solution {ans1}")
print(f"Part 2 solution {ans2}")