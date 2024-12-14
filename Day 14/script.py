import re
from collections import defaultdict
from functools import reduce

WIDTH =  101
HEIGHT =  103
mid_x = (WIDTH - 1)//2
mid_y = (HEIGHT -1)//2


def part_2(robots, velocities):
    for time in range(6870,6871):
        canvas = []
        for i in range(WIDTH):
            canvas.append([])
            for j in range(HEIGHT):
                canvas[-1].append(' ')
        for i, robot in enumerate(robots):
            x, y = robot
            vx, vy = velocities[i]
            new_x, new_y = (x + time * vx) % WIDTH, (y + time * vy) % HEIGHT
            canvas[new_x][new_y] = 'O'
        for i in canvas:
            print(''.join(i))
        print('-' * WIDTH)

def part_1(robots, velocities):
    ans = 0
    quadrant_counts = defaultdict(int)
    for i, robot in enumerate(robots):
        x, y = robot
        vx, vy = velocities[i]
        new_x, new_y = (x + 100 * vx) % WIDTH, (y + 100 * vy) % HEIGHT
        print(new_x, new_y)
        if new_x == mid_x or new_y == mid_y:
            continue
        if new_x <  mid_x and new_y < mid_y:
            quadrant_counts['1'] += 1
        elif new_x > mid_x and new_y < mid_y:
            quadrant_counts['2'] += 1
        elif new_x < mid_x and new_y > mid_y:
            quadrant_counts['3'] += 1
        elif new_x > mid_x and new_y > mid_y:
            quadrant_counts['4'] += 1
    print(quadrant_counts)
    ans = reduce(lambda acc, x: acc * x, quadrant_counts.values(), 1)
    return ans

robots = []
velocities = []
num_regex = r"(-?\d+)"
with open('./inputs.txt', 'r') as f:
  for line in f:
    cor = list(map(lambda x: int(x), re.findall(num_regex, line)))
    # robots[(cor[0], cor[1])] += 1
    robots.append((cor[0],cor[1]))
    velocities.append((cor[2], cor[3]))

print(part_1(robots, velocities))
print(part_2(robots, velocities))