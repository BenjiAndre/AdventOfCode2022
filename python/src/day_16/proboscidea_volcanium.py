import time
import re

def parse(data):
    p = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"
    valves = []
    for line in data:
        caught = re.match(p, line)
        valve = caught.group(1)
        flow = int(caught.group(2))
        neighbours = [valve.strip() for valve in caught.group(3).split(',')]
        valves.append((valve, flow, neighbours))

    return sorted(valves, key=lambda x: -x[1])


def main():

    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    valves = parse(data)

    labels = {valve: i for i, (valve, _, _) in enumerate(valves)}
    flow = [f for (_, f, _) in valves]
    adj = [[labels[tunnel] for tunnel in tunnels] for (_, _, tunnels) in valves]

    m = next(i for i, (_, flow, _) in enumerate(valves) if flow == 0)
    mm = 1 << m
    
    opt = [[[0] * mm for _ in range(len(valves))] for _ in range(30)]

    for t in range(1, 30):
        for i in range(len(valves)):
            ii = 1 << i
            for x in range(mm):
                tmp = opt[t][i][x]
                if ii & x != 0 and t >= 2:
                    tmp = max(tmp, opt[t-1][i][x - ii] + flow[i] * t)
                opt[t][i][x] = max(tmp, max(opt[t-1][j][x] for j in adj[i]))

    start = labels["AA"]
    part_1 = opt[29][start][mm-1];
    print(f"Part 1: {part_1}")
    part_2 = max(opt[25][start][x] + opt[25][start][mm-1-x] for x in range(mm//2))
    print(f"Part 2: {part_2}")



if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds")

