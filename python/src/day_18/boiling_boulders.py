import time

def sides(cube):
    x, y, z = cube
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)] 

def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()
    lava_drops = set()
    for cube in data:
        lava_drops.add(tuple(map(int, cube.split(','))))

    surface1 = sum(1 for c in lava_drops for side in sides(c) if side not in lava_drops)
    print(f"Part 1: {surface1}")

    max_val = max(max(c) for c in lava_drops) + 1
    seen = set()
    stack = [(0,0,0)]
    while stack:
        cube = stack.pop()
        for side in sides(cube):
            if side not in seen and side not in lava_drops and all(-1 <= c <= max_val for c in side):
                seen.add(side)
                stack.append(side)

    surface2 = sum(1 for c in lava_drops for side in sides(c) if side in seen)
    print(f"Part 2: {surface2}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
