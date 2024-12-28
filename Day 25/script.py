


locks = []
keys = []
with open('./inputs.txt', 'r') as f:
    schematics = [block.splitlines() for block in f.read().strip().split("\n\n")]
    locks = []
    keys = []

    for schematic in schematics:
        if "#" in schematic[0]: 
            locks.append(schematic[1:])
        elif "#" in schematic[-1]:
            keys.append(schematic[:-1])

def parse_heights(schematic, lock=True):
    num_rows = len(schematic)
    num_cols = len(schematic[0])
    heights = []

    for col in range(num_cols):
        height = 0
        for row in range(num_rows):
            if (lock and schematic[row][col] == '#') or (not lock and schematic[-(row + 1)][col] == '#'):
                height += 1
            elif lock and schematic[row][col] == '.':
                break 
        heights.append(height)

    return heights

def part_1(locks, keys):
    lock_heights = [parse_heights(lock) for lock in locks]
    key_heights = [parse_heights(key, lock=False) for key in keys]

    print(lock_heights)
    print(key_heights)
    fitting_pairs = 0
    total_height = 5

    for lock in lock_heights:
        for key in key_heights:
            fits = all(lock[i] + key[i] <= total_height for i in range(len(lock)))
            if fits:
                fitting_pairs += 1

    return fitting_pairs

print(part_1(locks, keys))