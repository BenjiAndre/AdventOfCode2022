import time

def examine_tree(grid, r, c):
    tree = grid[r][c]
    invisible, score = True, 1
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dr, dc in directions:
        i, visible = 0, True
        row, col = r, c
        while 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
            next_value = grid[row + dr][col + dc]
            i += 1
            if tree <= next_value:
                visible = False
                break
            row += dr
            col += dc
        if visible:
            invisible = False
        score *= i
    return not invisible, score

def main():
    with open("input/input.txt", "r") as f:
        data = [list(map(int, line)) for line in f.read().splitlines()]


    result = (0, 0)
    for r in range(len(data)):
        for c in range(len(data[0])):
            visible, score = examine_tree(data, r, c)
            result = (result[0] + int(visible), max(result[1], score))

    print(f"Part 1: Number of visible trees : {result[0]}")
    print(f"Part 2: Best scenic score of the forest : {result[1]}")
    

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
