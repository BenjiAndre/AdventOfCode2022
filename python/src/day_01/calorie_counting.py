import time

def main():
    with open("input/input.txt", 'r') as f:
        elf_meals = f.read().split("\n\n")

    elf_calories = []
    for elf in elf_meals:
        calories = sum(map(int, elf.splitlines()))
        elf_calories.append(calories)

    print(f"Part 1: {max(elf_calories)}")
    elf_calories = sorted(elf_calories)
    print(f"Part 2: {sum(elf_calories[-3:])}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.04f} seconds")
