word = "MAS"
len_word = len(word)


def check(x1, y1, x2, y2, metric, selected_pair1, selected_pair2):
  matches = 0
  row = len(metric)
  col = len(metric[0])
  for k in range(2):
    matched_len = 1
    new_x1, new_y1 = x1 + selected_pair1[k][0], y1 + selected_pair1[k][1]
    new_x2, new_y2 = x2 + selected_pair2[k][0], y2+selected_pair2[k][1]
    while matched_len < len_word:
      if 0 <= new_x1 < row and 0 <= new_x2 < row and 0 <= new_y1 < col and 0 <= new_y2 < col:
        if metric[new_x1][new_y1] == word[matched_len] and metric[new_x2][new_y2] == word[matched_len]:
          new_x1, new_y1 = new_x1 + selected_pair1[k][0], new_y1+selected_pair1[k][1]
          new_x2, new_y2 = new_x2 + selected_pair2[k][0], new_y2+selected_pair2[k][1]
          matched_len += 1
        else:
          break
      else:
        break
    if matched_len == len_word:
        matches += 1
  return matches

def part_2 (metric):
  matches = 0
  row = len(metric)
  col = len(metric[0])
  forward_pairs = [[1, 1], [-1, 1]]
  backward_pairs = [[1, 1], [1, -1]]
  horiz_pairs = [[1, -1], [-1, -1]]
  vertical_pairs = [[-1, 1], [-1, -1]]
  
  for i in range(row):
    for j in range(col):
      if metric[i][j] == word[0]:
        if (j + 2) < col and metric[i][j+2] == word[0]:
          x2, y2 = i, j+2
          matches += check(i, j, x2, y2, metric, forward_pairs, horiz_pairs)
        if i + 2 < row and metric[i+2][j] == word[0]:
          x2, y2 = i+2, j
          matches += check(i, j, x2, y2, metric, backward_pairs, vertical_pairs)
        
  return matches

def part_1(metric):
  matches = 0
  row = len(metric)
  col = len(metric[0])

  x = [-1, -1, -1, 0, 0, 1, 1, 1]
  y = [-1, 0, 1, -1, 1, -1, 0, 1]

  word = "XMAS"
  len_word = len(word)
  for i in range(row):
    for j in range(col):
      if metric[i][j] == word[0]:
        for temp in range(0, 8):
          matched_len = 1
          new_x, new_y = int(i + x[temp]), int(j + y[temp])
          while matched_len < len_word:
            if new_x >= row or new_x < 0 or new_y >= col or new_y < 0:
              break    
            if metric[new_x][new_y] == word[matched_len]:
              new_x, new_y = int(new_x + x[temp]), int(new_y + y[temp])
              matched_len += 1
            else: 
              break
          if matched_len == len_word:
            matches += 1
  return matches

metric = []
with open('./inputs.txt', 'r') as f:
  for line in f:
    line = list(line.strip())
    metric.append(line)

print(part_1(metric)) # 2468
print(part_2(metric)) # 1864