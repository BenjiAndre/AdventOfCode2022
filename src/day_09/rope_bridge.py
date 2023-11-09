import time
from dataclasses import dataclass

@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

VECTORS = {
    'U': Coord(0, 1),
    'R': Coord(1, 0),
    'D': Coord(0, -1),
    'L': Coord(-1, 0)
}

IN_RANGE = [Coord(x, y) for x in range(-1, 2) for y in range (-1, 2)]

def main():
    with open("input/input.txt", "r") as f:
        lines = f.read().splitlines()
        data = [(d, int(v)) for d, v in [line.split() for line in lines]]

    sim1 = simulation([Coord(0,0) for _ in range(2)], data);
    sim2 = simulation([Coord(0,0) for _ in range(10)], data);

    print(f"Part 1: Number of visited positions : {sim1}")
    print(f"Part 2: Number of visited positions : {sim2}")


def simulation(knots: list[Coord], data: list[tuple[str, int]]) -> int:
    
    visited: set[Point] = set()
    visited.add(knots[0]) # Add the starting position
    for vector, norm in data:
        for _ in range(norm):

            knots[0] += VECTORS[vector] # Move the head

            for i in range(1, len(knots)):
                distance = knots[i-1] - knots[i]
                if distance in IN_RANGE:
                    continue
                else:
                    knots[i] += get_next_move(distance)
                    visited.add(knots[-1])

    return len(visited)


    
def get_next_move(vector: Coord) -> Coord:
    x, y = 0, 0
    move_x, move_y = False, False

    if vector.x == 0:
        move_y = True
    elif vector.y == 0:
        move_x = True
    else:
        move_x, move_y = True, True

    if move_x:
        x = 1 if vector.x > 0 else -1
    if move_y:
        y = 1 if vector.y > 0 else -1

    return Coord(x, y)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
