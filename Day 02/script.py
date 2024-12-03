def validate(report):
  increase = all(i > j for i, j in zip(report, report[1:]))
  decrease = all(i < j for i, j in zip(report, report[1:]))
  difference = all(abs(i - j) <= 3 and abs(i - j) >= 1 for i, j in zip(report, report[1:]))
  return (increase or decrease) and difference

def fix(report):
  for i in range(len(report)):
    tmp = report[:]
    del tmp[i]
    if validate(tmp):
      return True
  return False

def part_1(reports):
  safe = 0
  for report in reports:
    if validate(report):
      safe += 1
  return safe

def part_2(reports):
  safe = 0
  for report in reports:
    if validate(report):
      safe += 1
    elif fix(report):
      safe += 1
  return safe

reports = []
with open('./inputs.txt', 'r') as f:
  for line in f:
    line = map(lambda x: int(x), line.strip().split())
    reports.append(list(line))

print(f"Part 1 ans: {part_1(reports)}")
print(f"Part 2 ans: {part_2(reports)}")