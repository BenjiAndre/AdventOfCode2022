import time

def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    # Process the data
    # --> Turns each line into a list of sets containing the tasks of each elf
    assignment_pairs = []
    for pairs in data:
        this_pair = pairs.split(',')
        assigments = []
        for tasks in this_pair:
            start, end = list(map(int, tasks.split("-")))
            assigments.append(set(range(start, end+1)))

        assignment_pairs.append(assigments)

    includes_count = sum(1 for tasks_1, tasks_2 in assignment_pairs
                if tasks_1 == tasks_2 or
                tasks_1 < tasks_2 or # tasks_1 subset of tasks_2
                tasks_2 < tasks_1) # tasks_2 subset of tasks_1

    print(f"Part 1: Number of assignment inclusions = {includes_count}")

    overlap_count = sum(1 for tasks_1, tasks_2 in assignment_pairs
                        if tasks_1 & tasks_2)

    print(f"Part 2: Numnber of assignment overlaps = {overlap_count}")








if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
