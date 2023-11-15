import time
from collections import deque

def solve(Co, Cc, Co1, Co2, Cg1, Cg2, T):
    best = 0
    # state if (ore, clay, obsidian, geodes, r1, r2, r3, r4, time)
    S = (0, 0, 0, 0, 1, 0, 0, 0, T)
    Q = deque([S])
    SEEN = set()
    while Q:
        state = Q.popleft()
        o,c,ob,g,r1,r2,r3,r4,t = state

        best = max(best, g)
        if t==0:
            continue
        
        # When we have enough material-robots to produce enough ore to make another robot each minute,
        # We do not need to make more ore, so we cap these values
        Core = max([Co, Cc, Co1, Cg1])
        if r1 >= Core:
            r1 = Core
        if r2 >= Co2:
            r2 = Co2
        if r3 >= Cg2:
            r3 = Cg2

        # If we have more than enough material, we cap these values because it doesn't change anything
        # And this way we can do set comparison to find the best value
        if o >= t * Core - r1 * (t-1):
            o = t * Core - r1 * (t-1)
        if c >= t * Co2 - r2 * (t-1):
            c = t * Co2 - r2 * (t-1)
        if ob >= t * Cg2 - r3 * (t-1):
            ob = t * Cg2 - r3 * (t-1)

        state = (o,c,ob,g,r1,r2,r3,r4,t)
        if state in SEEN:
            continue
        SEEN.add(state)

        Q.append((o+r1,c+r2,ob+r3,g+r4,r1,r2,r3,r4,t-1))
        if o>=Co: # buy ore
            Q.append((o-Co+r1, c+r2, ob+r3, g+r4, r1+1,r2,r3,r4,t-1))
        if o>=Cc:
            Q.append((o-Cc+r1, c+r2, ob+r3, g+r4, r1,r2+1,r3,r4,t-1))
        if o>=Co1 and c>=Co2:
            Q.append((o-Co1+r1, c-Co2+r2, ob+r3, g+r4, r1,r2,r3+1,r4,t-1))
        if o>=Cg1 and ob>=Cg2:
            Q.append((o-Cg1+r1, c+r2, ob-Cg2+r3, g+r4, r1,r2,r3,r4+1,t-1))

    return best

def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    quality_level_sum1 = 0
    quality_level_sum2 = 1
    for i, line in enumerate(data):
        words = line.split()
        id_ = int(words[1][:-1]) # id of the blueprint
        ore_cost = int(words[6])
        clay_cost = int(words[12])
        obsidian_cost_ore, obsidian_cost_clay = int(words[18]), int(words[21])
        geode_cost_ore, geode_cost_clay = int(words[27]), int(words[30])
        best = solve(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, 24)
        quality_level_sum1 += id_ * best
        if i<3:
            s2 = solve(ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay,32)
            quality_level_sum2 *= s2

    print(f"Part 1: quality level sum: {quality_level_sum1}")
    print(f"Part 2: quality level sum: {quality_level_sum2}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds")
