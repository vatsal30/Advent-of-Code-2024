import re
from fractions import Fraction

def part_2(data, targets):
  ans = 0
  for i, target in enumerate(targets):
    point_a, point_b = data[i]
    target_x = target[0] + 10000000000000
    target_y = target[1] + 10000000000000
    A = Fraction(-(point_b[1]*target_x-point_b[0]*target_y), (point_a[1]*point_b[0]-point_a[0]*point_b[1]))
    B = Fraction((point_a[1]*target_x-point_a[0]*target_y), (point_a[1]*point_b[0]-point_a[0]*point_b[1]))
    if A.denominator != 1 or B.denominator != 1:
      continue
    ans += 3*A + B
  return ans

def part_1(data, targets):
  ans = 0
  for i, target in enumerate(targets):
    point_a, point_b = data[i]
    n1 = target[0] // point_a[0]
    n2 = target[1] // point_a[1]
    n = min(max(n1, n2), 100)
    m1 = target[0] // point_b[0]
    m2 = target[1] // point_b[1]
    m = min(max(m1,m2), 100)
    for i in range(n, -1, -1):
      for j in range(m, -1, -1):
        x = point_a[0] * i + point_b[0]*j
        y = point_a[1] * i + point_b[1]*j
        if target[0] == x and target[1] == y:
          ans += i * 3 + j
  return ans

data = []
targets = []
num_regex = r"\d+"
with open('./inputs.txt', 'r') as f:
  file = f.readlines()
  n = len(file)
  i = 0
  while i < n:
    point_a = list(map(lambda x: int(x), re.findall(num_regex, file[i])))
    i += 1
    point_b = list(map(lambda x: int(x), re.findall(num_regex, file[i])))
    i+=1
    target_x_y = list(map(lambda x: int(x), re.findall(num_regex, file[i])))
    i +=2
    data.append([point_a, point_b])
    targets.append(target_x_y)
  print(data)
  print(targets)
print(part_1(data, targets))
print(part_2(data, targets))