import time
from dataclasses import dataclass

@dataclass(frozen=True)
class Coord():
    x: int
    y: int

def get_rocks(data: list[str]) -> set[Coord]:
    rocks = set()
    for rock_lines in data:
        """ Transform data that looks like : 498,4 -> 498,6
            Into data that looks like : [Coord(498,4), Coord(498,6)]"""
        points = rock_lines.split(" -> ")
        raw_rock_lines = [raw.split(",") for raw in points]
        rock_lines = [Coord(int(x), int(y)) for x, y in raw_rock_lines]

        for i in range(len(rock_lines)-1):
            s_x, e_x = sorted((rock_lines[i].x, rock_lines[i+1].x))
            s_y, e_y = sorted((rock_lines[i].y, rock_lines[i+1].y))
            if s_x == e_x:
                for y in range(s_y, e_y + 1):
                    rocks.add(Coord(s_x, y))
            else:
                for x in range(s_x, e_x + 1):
                    rocks.add(Coord(x, s_y))

    return rocks

class Cave():

    VECTORS = [Coord(0,1), Coord(-1,1), Coord(1, 1)]

    def __init__(self, rocks):
        self.rocks = rocks
        self.sand = set()
        self.max_y = max(rock.y for rock in rocks)
        self.floor = self.max_y + 2

    def in_void(self, unit: Coord):
        return not (0 <= unit.y <= self.max_y + 2)


    def drop_sand(self, floor=False):
        s = Coord(500, 0)
        falling = True
        while falling:
            if self.in_void(s):
                return False
            for v in self.VECTORS:
                candidate = Coord(s.x + v.x, s.y + v.y)
                if candidate not in self.sand and candidate not in self.rocks:
                    if floor and candidate.y == self.floor:
                        falling = False
                        break
                    s = candidate
                    break
            else:
                falling = False

        self.sand.add(s)
        return True


def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    rocks = get_rocks(data)
    cave = Cave(rocks)
    units = 0
    while(cave.drop_sand()):
        units += 1
    print(f"Part 1: Number of units of sand at rest : {units}")
    while(Coord(500, 0) not in cave.sand):
        cave.drop_sand(True)
        units += 1
    print(f"Part 2: Number of units of sand at rest before reaching source : {units}")



    

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
