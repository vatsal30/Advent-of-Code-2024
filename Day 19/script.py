
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

class TrieNode:
  def __init__(self):
      self.children = {}
      self.is_end = False

class Trie:
  def __init__(self):
      self.root = TrieNode()

  def insert(self, pattern):
      node = self.root
      for char in pattern:
          if char not in node.children:
              node.children[char] = TrieNode()
          node = node.children[char]
      node.is_end = True 

  def search(self, design, start):
     
      node = self.root
      results = []
      for i in range(start, len(design)):
          char = design[i]
          if char not in node.children:
              break
          node = node.children[char]
          if node.is_end:
              results.append(i + 1)  
      return results
  
def part_1(designs, patterns):
  ans = 0
  trie = Trie()
  for pattern in patterns:
      trie.insert(pattern)
  for design in designs:
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
      if dp[i]:
        matches = trie.search(design, i)
        for end_index in matches:
            dp[end_index] = True
    if dp[n]:
      ans += 1
  
  return ans

def part_2(designs, patterns):
  ans = 0
  trie = Trie()
  for pattern in patterns:
      trie.insert(pattern)
  for design in designs:
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
      if dp[i]:
        matches = trie.search(design, i)
        for end_index in matches:
            dp[end_index] += dp[i]
    if dp[n]:
      ans += dp[n]
  
  return ans
print(part_1(designs, patterns))
print(part_2(designs, patterns))