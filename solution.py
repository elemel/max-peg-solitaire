from collections import deque
import sys


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def print_path(grid, parents):
    parent = parents.get(grid)

    if parent:
        print_path(parent, parents)
        print()

    for row in grid:
        print(row)


grid = tuple(line.rstrip() for line in sys.stdin)
peg_count = sum(row.count('o') for row in grid)

queue = deque([(peg_count, grid)])
parents = {grid: None}

max_peg_count = 0
max_grid = None

while queue:
    peg_count, grid = queue.popleft()

    if peg_count <= max_peg_count:
        continue

    done = True

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'o':
                for dx, dy in DIRECTIONS:
                    if (0 <= y + 2 * dy < len(grid) and
                        0 <= x + 2 * dx < len(grid[y + 2 * dy]) and
                        grid[y + dy][x + dx] == 'o' and
                        grid[y + 2 * dy][x + 2 * dx] == '.'):

                        done = False

                        new_grid = list(list(row) for row in grid)
                        new_grid[y][x] = '.'
                        new_grid[y + dy][x + dx] = '.'
                        new_grid[y + 2 * dy][x + 2 * dx] = 'o'
                        new_grid = tuple(''.join(row) for row in new_grid)

                        if new_grid not in parents:
                            parents[new_grid] = grid
                            queue.append((peg_count - 1, new_grid))

    if done:
        if peg_count > max_peg_count:
            max_peg_count = peg_count
            max_grid = grid

print_path(max_grid, parents)
print()
print(max_peg_count, len(parents))
