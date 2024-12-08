
def find_antennas(data):
    antennas = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] != '.':
                antennas.append((x, y, data[x][y]))
    return antennas

def part_2(data, antennas, freq_map):
    rows = len(data)
    cols = len(data[0])
    antinode_positions = set()
    
    for freq, positions in freq_map.items():
        for i in range(len(positions)):
            for j in range((i + 1), len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dist_x, dist_y = abs(x2 - x1), abs(y2 - y1)
                flag = True
                multi = 1
                while flag:
                    flag = False
                    if x2 > x1 and y2 > y1:
                        antinode1 = (x1 - (multi * dist_x), y1 - (multi *dist_y))
                        antinode2 = (x2 + (multi * dist_x), y2 + (multi *dist_y))
                    elif x2 > x1 and y2 < y1:
                        antinode1 = (x1 - (multi *dist_x), y1 + (multi *dist_y))
                        antinode2 = (x2 + (multi *dist_x), y2 - (multi *dist_y))
                    elif x2 < x1 and y2 < y1:
                        antinode1 = (x1 + (multi *dist_x), y1 + (multi *dist_y))
                        antinode2 = (x2 - (multi *dist_x), y2 - (multi *dist_y))
                    else:
                        antinode1 = (x1 + (multi *dist_x), y1 - (multi *dist_y))
                        antinode2 = (x2 - (multi *dist_x), y2 + (multi *dist_y))

                    
                    if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                        antinode_positions.add(antinode1)
                        data[antinode1[0]][antinode1[1]] = '#'
                        flag = True
                    if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                        antinode_positions.add(antinode2) 
                        data[antinode2[0]][antinode2[1]] = '#'
                        flag = True
                    multi += 1
    for x,y,freq in antennas:
        if len(freq_map[freq]) > 1:
            antinode_positions.add((x,y))
    return len(antinode_positions)

def part_1(data, antennas, freq_map):
    rows = len(data)
    cols = len(data[0])
    antinode_positions = set()
    for freq, positions in freq_map.items():
        for i in range(len(positions)):
            for j in range((i + 1), len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dist_x, dist_y = abs(x2 - x1), abs(y2 - y1)
                if x2 > x1 and y2 > y1:
                    antinode1 = (x1 - dist_x, y1 - dist_y)
                    antinode2 = (x2 + dist_x, y2 + dist_y)
                elif x2 > x1 and y2 < y1:
                    antinode1 = (x1 - dist_x, y1 + dist_y)
                    antinode2 = (x2 + dist_x, y2 - dist_y)
                elif x2 < x1 and y2 < y1:
                    antinode1 = (x1 + dist_x, y1 + dist_y)
                    antinode2 = (x2 - dist_x, y2 - dist_y)
                else:
                    antinode1 = (x1 + dist_x, y1 - dist_y)
                    antinode2 = (x2 - dist_x, y2 + dist_y)
                if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                    antinode_positions.add(antinode1)
                if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                    antinode_positions.add(antinode2)
    return len(antinode_positions)

data = []
freq_map = {}
with open('./inputs.txt', 'r') as f:
    for line in f:
      data.append(list(line.strip()))
    antennas = find_antennas(data)
    for x,y,freq in antennas:
        if freq not in freq_map:
            freq_map[freq] = []
        freq_map[freq].append((x,y))

print(part_1(data, antennas, freq_map))
print(part_2(data, antennas, freq_map))
