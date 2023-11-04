import time

HAND = {
    "ROCK": "A",
    "PAPER": "B",
    "SCISSORS": "C"
}

REQUIRED = {
    "LOSE": "X",
    "DRAW": "Y",
    "WIN": "Z"
}

SCORES = {
        HAND["ROCK"]: 1,
        HAND["PAPER"]: 2,
        HAND["SCISSORS"]: 3,
        "LOSE": 0,
        "DRAW": 3,
        "WIN": 6
}

# Put Rock Paper Scissors rules in directory to avoid if/elif/else statements
RULES = {
    # Part 1
    (HAND["ROCK"], HAND["SCISSORS"]): SCORES["LOSE"],
    (HAND["ROCK"], HAND["ROCK"]): SCORES["DRAW"],
    (HAND["ROCK"], HAND["PAPER"]): SCORES["WIN"],
    (HAND["PAPER"], HAND["ROCK"]): SCORES["LOSE"],
    (HAND["PAPER"], HAND["PAPER"]): SCORES["DRAW"],
    (HAND["PAPER"], HAND["SCISSORS"]): SCORES["WIN"],
    (HAND["SCISSORS"], HAND["PAPER"]): SCORES["LOSE"],
    (HAND["SCISSORS"], HAND["SCISSORS"]): SCORES["DRAW"],
    (HAND["SCISSORS"], HAND["ROCK"]): SCORES["WIN"],

    # Part 2
    (HAND["ROCK"], REQUIRED["LOSE"]): SCORES[HAND["SCISSORS"]],
    (HAND["ROCK"], REQUIRED["DRAW"]): SCORES[HAND["ROCK"]],
    (HAND["ROCK"], REQUIRED["WIN"]): SCORES[HAND["PAPER"]],
    (HAND["PAPER"], REQUIRED["LOSE"]): SCORES[HAND["ROCK"]],
    (HAND["PAPER"], REQUIRED["DRAW"]): SCORES[HAND["PAPER"]],
    (HAND["PAPER"], REQUIRED["WIN"]): SCORES[HAND["SCISSORS"]],
    (HAND["SCISSORS"], REQUIRED["LOSE"]): SCORES[HAND["PAPER"]],
    (HAND["SCISSORS"], REQUIRED["DRAW"]): SCORES[HAND["SCISSORS"]],
    (HAND["SCISSORS"], REQUIRED["WIN"]): SCORES[HAND["ROCK"]]
}

def main():
    with open("input/input.txt" ,"r") as f:
        data = f.read().splitlines()
    
    # Make a list of each rounds
    rounds = []
    for r in data:
        rounds.append(r.split())

    score = play_strategy_guide_1(rounds) # Part 1
    print(f"Part 1: Strategy Guide Score = {score}")
    score = play_strategy_guide_2(rounds) # Part 2
    print(f"Part 2: Strategy Guide Score = {score}")

def play_strategy_guide_1(rounds: list):
    score = 0
    xyz_to_rps = {"X": HAND["ROCK"], "Y": HAND["PAPER"], "Z": HAND["SCISSORS"]}
    for r in rounds:
        their_hand, my_hand = r
        my_hand = xyz_to_rps[my_hand]

        score += SCORES[my_hand] + RULES[(their_hand, my_hand)]

    return score

def play_strategy_guide_2(rounds):
    score = 0
    xyz_to_ldw = {"X": SCORES["LOSE"], "Y": SCORES["DRAW"], "Z": SCORES["WIN"]}
    for r in rounds:
        their_hand, my_goal = r

        score += xyz_to_ldw[my_goal] + RULES[(their_hand, my_goal)]

    return score



if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.04f} seconds")

