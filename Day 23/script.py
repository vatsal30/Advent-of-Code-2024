from collections import defaultdict
from itertools import combinations
from functools import reduce

data = []
with open('./inputs.txt', 'r') as f:
    for line in f:
        data.append(line.strip().split('-'))

def part1():
    pair_dict = defaultdict(set)
    for cm1, cm2 in data:
      pair_dict[cm1].add(cm2)
      pair_dict[cm2].add(cm1)
    
    pairs = set()
    
    for cm in pair_dict:
        connections = pair_dict[cm]
        for connection in connections:
          common_connections = connections & pair_dict[connection]
          for common_connection in common_connections:
            pair = tuple(sorted([cm, connection, common_connection]))
            pairs.add(pair)
    
    pairs_with_t = [
        pair for pair in pairs if any(cm.startswith('t') for cm in pair)
    ]
    return len(pairs_with_t)

def part2():
    pair_dict = defaultdict(set)
    for cm1, cm2 in data:
      pair_dict[cm1].add(cm2)
      pair_dict[cm2].add(cm1)
    
    pairs = []
    for conn in data:
      pairs.append(tuple(sorted(conn)))
    
    while True:
      new_pairs = []
      for pair in pairs:
        connections = reduce(set.intersection, map(lambda x: pair_dict[x], pair))
        for conn in connections:
          if conn > pair[-1]:
            new_pairs.append(pair + (conn, ))
      if new_pairs:
        pairs = new_pairs
      else:
        return ','.join(pairs[0])
             
print(part1())
print(part2())
        
                

            