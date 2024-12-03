import re

def multiply(mul):
  digits = re.findall(r"\d{1,3}", mul)
  return int(digits[0]) * int(digits[1])

def part_01(memory):
  regex_to_match_mul = r"mul\(\d{1,3},\d{1,3}\)"
  matches = re.findall(regex_to_match_mul, memory)
  ans = 0
  for match in matches:
    ans += multiply(match)
  return ans

def part_02(memory):
  regex_to_match_mul = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"
  matches = re.findall(regex_to_match_mul, memory)
  ans = 0
  flag = True
  for match in matches:
    if match == "do()":
      flag = True 
      continue
    if match == "don't()":
      flag = False
      continue
    if flag:
      ans += multiply(match)
  return ans


with open('./inputs.txt', 'r') as f:
  memory = f.read()

print(f"Part 01 ans: {part_01(memory)}")
print(f"Part 02  ans: {part_02(memory)}")