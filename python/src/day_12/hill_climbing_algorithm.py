import time
from collections import deque

def find_pos(data, val):
    """ Finds the position of the value val in data"""
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if data[i][j] == val:
                return i, j

def find_all_pos(data, val):
    """ Finds the position of all the values val in data"""
    positions = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if data[i][j] == val:
                positions.append((i,j))
    return positions

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque((x, y, 0) for x, y in start)

    while queue:
        x, y, length = queue.popleft()

        if (x, y) == goal:
            return length

        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                square = ord(grid[nx][ny])
                if ord(grid[x][y]) + 1 >= square and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, length + 1))

    return None

def main():
    with open("input/input.txt", "r") as f:
        grid = [list(line) for line in f.read().splitlines()]

    sx, sy = find_pos(grid, 'S')
    ex, ey = find_pos(grid, 'E')

    grid[sx][sy] = 'a'
    grid[ex][ey] = 'z'

    positions = [(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 'a']
    res1 = bfs(grid, [(sx, sy)], (ex, ey))
    res2 = bfs(grid, positions, (ex, ey))
    print(f"Part 1: Fewest possible steps : {res1}")
    print(f"Part 2: Fewest possible steps on coke : {res2}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
