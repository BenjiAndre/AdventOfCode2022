import time

INTERESTING_CYCLES = [20, 60, 100, 140, 180, 220]

class CrtComputer():
    def __init__(self, data: list[str]) -> None:
        self.x = 1
        self._instructions = self._data_to_instructions(data)
        self._pc = 0 # Program Counter
        self.cycle = 0
        self._current = [] # The current instruction
        self.running = True # Set to False when all instructions have been ran
        self._display = [[" " for _ in range(40)] for _ in range(6)]


    @property
    def signal_strength(self) -> int:
        return self.cycle * self.x

    def _data_to_instructions(self, data: list[str]) -> list[tuple[str, int]]:
        """ Creates a list of instruction in the following format:
                        [[instr, val], [], ...] 
        """
        instructions = []
        for line in data:
            cmd = line.split()
            instruction = cmd[0]
            arg = None
            if len(cmd) > 1:
                arg = int(cmd[1])
            instructions.append((instruction, arg))
 
        return instructions

    def tick(self):
        if self._current:
            self._current[1] -= 1 # Process instruction
            
            if self._current[1] == 0:
                instruction = self._current[0]
                self.__getattribute__(f"{instruction[0]}")(instruction)
                self._next_instruction() # If instruction is finished start next one
        else:
            self._next_instruction()

        self.cycle += 1

    def _next_instruction(self):
        instruction = self._instructions[self._pc]

        if instruction[0] == "addx":
            self._current = [instruction, 2]
        elif instruction[0] == "noop":
            self._current = [instruction, 1]

        self._pc += 1
        if self._pc == len(self._instructions):
            self.running = False

    def addx(self, instruction: tuple):
        self.x += instruction[-1]

    def noop(self, _: tuple):
        return




def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    display = [["." for _ in range(40)] for _ in range(6)]
    signal_strength = 0
    computer = CrtComputer(data)

    display_row = -1
    while computer.running:
        # Setup display position
        row_position = (computer.cycle-1) % 40
        if row_position == 0:
            display_row += 1
        
        if row_position in range(computer.x-1, computer.x+2):
            display[display_row][row_position] = "#"

        computer.tick()

        if computer.cycle in INTERESTING_CYCLES:
            signal_strength += computer.signal_strength

    print(f"Part 1: Sum of interesting singal stregth : {signal_strength}")
    print(f"Part 2: Signal Rendering")
    print("\n".join("".join(row) for row in display))

    





if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
