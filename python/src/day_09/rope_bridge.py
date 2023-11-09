import time

VECTORS = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}

IN_RANGE = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]

def simulation(knots, data):
    visited = set(knots)
    
    for vector, norm in data:
        for _ in range(norm):
            direction = VECTORS[vector]
            knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])

            for i in range(1, len(knots)):
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]

                distance = dx, dy
                if distance not in IN_RANGE:
                    x = knots[i][0] + get_next_move(distance)[0]
                    y = knots[i][1] + get_next_move(distance)[1]
                    knots[i] = (x, y) 
                    visited.add(knots[-1])

    return len(visited)

def get_next_move(vector):
    x = 1 if vector[0] > 0 else -1 if vector[0] < 0 else 0
    y = 1 if vector[1] > 0 else -1 if vector[1] < 0 else 0
    return (x, y)

def main():
    with open("input/input.txt", "r") as f:
        lines = f.read().splitlines()
        data = [(d, int(v)) for d, v in [line.split() for line in lines]]

    sim1 = simulation([(0, 0) for _ in range(2)], data)
    sim2 = simulation([(0, 0) for _ in range(10)], data)

    print(f"Part 1: Number of visited positions: {sim1}")
    print(f"Part 2: Number of visited positions: {sim2}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
