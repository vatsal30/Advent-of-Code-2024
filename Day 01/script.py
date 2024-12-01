from collections import defaultdict

def part_1(col1, col2):
    col1.sort()
    col2.sort()
    ans = 0
    for num1, num2 in list(zip(col1, col2)):
        ans += abs(num2 - num1)
    return ans

def part_2(col1, counts):
    sum = 0
    for num in col1:
        sum += counts[num] * num
    return sum


col1 = []
col2 = []
counter = defaultdict(int)

with open('./inputs.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        col1.append(int(line[0]))
        col2.append(int(line[1]))
        counter[int(line[1])] += 1

ans1 = part_1(col1, col2)
ans2 = part_2(col1, counter)
print(ans1)
print(ans2)