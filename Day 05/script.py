from collections import defaultdict

def fix_order(order_hash, order):
  # Kind of insertion sort based on order_hash
  n = len(order)
  for i in range(n-2, -1, -1):
    j = i+1
    while j < n:
      if order[j] in order_hash[order[j-1]]:
        order[j], order[j-1] = order[j-1], order[j]
        j += 1
      else:
        break
  return order


def part_2(order_hash, incorrect_orders):
  ans = 0
  for order in incorrect_orders:
      n = len(order)
      sorted_order = fix_order(order_hash, order)
      ans += sorted_order[n//2]
  return ans 

      
def part_1(order_hash, orders):
    ans = 0
    incorrect_orders = []
    for order in orders:
      n = len(order)
      mid = order[n // 2]
      is_correct = True
      for i in range(n-2, -1, -1):
        j = i + 1
        while j < n:
          if order[j] in order_hash[order[i]]:
            is_correct = False
            break
          j += 1
        if not is_correct:
          break
      if is_correct:
          ans += mid
      else:
         incorrect_orders.append(order)
    return incorrect_orders, ans

order_hash = defaultdict(list)
data = []
with open('./inputs.txt', 'r') as f:
    start_data = False
    for line in f:
        if line == '\n':
           start_data = True
           continue
        if start_data:
          data.append(list(map(lambda x: int(x), line.strip().split(','))))
        else:
           num1, num2 = list(map(lambda x: int(x), line.strip().split('|')))
           order_hash[num2].append(num1)

incorrect_data, ans1 = part_1(order_hash, data)
print(f"Part 1: {ans1}")
ans2 = part_2(order_hash, incorrect_data)
print(f"Part 2: {ans2}")