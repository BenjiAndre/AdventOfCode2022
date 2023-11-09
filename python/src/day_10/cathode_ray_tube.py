import time




def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    x, cycle, signal_strength, signal_render = 1, 0, 0, ""

    def tick():
        nonlocal cycle, signal_strength, signal_render
        if cycle % 40 == 0:
            signal_render += '\n'
        signal_render += '█' if abs(x - cycle % 40) < 2 else ' '
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signal_strength += cycle * x

    for line in data:
        tick()
        if len(line) > 4:
            tick()
            x += int(line[5:])

    print(f"Part 1: Sum of interesting singal strength : {signal_strength}")
    print(f"Part 2: Signal Rendering :\n {signal_render}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
