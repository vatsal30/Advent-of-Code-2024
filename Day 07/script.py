from itertools import product

def check_eval(predic, nums, operations):
    result = nums[0]
    for i, op in enumerate(operations):
        if op == '*':
            result *= nums[i+1]
        elif op == '+':
            result += nums[i+1]
        elif op == '|':
            result = int(str(result) + str(nums[i+1]))
    return predic == result

def part_2(data):
    ans = 0
    for predic in data:
        nums = data[predic]
        combinations = product('+*|', repeat=len(nums)-1)
        flag = False
        for combination in combinations:
            if check_eval(predic, nums, combination):
                flag = True
                break
        if flag:
            ans += predic
    return ans  

def part_1(data):
    ans = 0
    for predic in data:
        nums = data[predic]
        combinations = product('+*', repeat=len(nums)-1)
        flag = False
        for combination in combinations:
            if check_eval(predic, nums, combination):
                flag = True
                break
        if flag:
            ans += predic
    return ans
    
data = {}
with open('./inputs.txt', 'r') as f:
    for line in f:
      predic, nums = list(line.strip().split(': '))
      predic = int(predic)
      nums = list(map(lambda x: int(x), nums.strip().split(' ')))
      data[predic] = nums

print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")