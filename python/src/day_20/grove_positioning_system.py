import time
from collections import deque

def mixing(data):
    length = len(data)
    for index in range(length):
        while data[0][0] != index:
            data.rotate(-1)
        
        i, rot = data.popleft()
        rotation = rot % (length - 1) # Since we popped an element
        data.rotate(-rotation)
        data.append((i, rot))

    return data

def main():
    with open("input/input.txt", "r") as f:
        data = list(map(int, f.read().splitlines()))  

    queue = deque(list(enumerate(data.copy())))
    mixed_data = mixing(queue)

    # Part 1
    all_values = [data[1] for data in mixed_data]
    part1 = 0
    for x in [1000, 2000, 3000]:
        val = all_values[(all_values.index(0) + x) % len(all_values)]
        part1 += val
    print(f"Part 1: {part1}")

    # Part 2
    new_data = [value * 811589153 for value in data]
    mixed_data = deque(list(enumerate(new_data)))
    for _ in range(10):
        mixed_data = mixing(mixed_data)
    
    all_values = [data[1] for data in mixed_data]
    part2 = 0
    for x in [1000, 2000, 3000]:
        val = all_values[(all_values.index(0) + x) % len(all_values)]
        part2 += val
    print(f"Part 2: {part2}")






    
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds")
