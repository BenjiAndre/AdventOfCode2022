import time
import ast

class Packet():
    """ Packet is made up of a value which is either a list or an int.
        If it is a list it can contain other lists
        It can be compared, and therefore sorted
    """
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        # Base case - both are integers
        if isinstance(self.value, int) and isinstance(other.value, int):
            if self.value < other.value:
                return True 
            if other.value < self.value:
                return False

        # if one int and one list
        if isinstance(self.value, int) and isinstance(other.value, list):
            new_item = Packet([self.value]) # convert this int to list
            return new_item < other
        if isinstance(self.value, list) and isinstance(other.value, int):
            new_item = Packet([other.value]) # convert other int to list
            return self < new_item
        
        # both are lists
        if isinstance(self.value, list) and isinstance(other.value, list):
            for l, r in zip(self.value, other.value): 
                if l == r:
                    continue # if the same, continue to next item
                
                # Else transform into Packet and compare
                return Packet(l) < Packet(r)
            
            # If we're here, then the iterator terminated before finding a difference
            return len(self.value) <= len(other.value)

def parse(line):
    left, right = line.splitlines()
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)
    return left, right

def get_packets(data):
    return [Packet(ast.literal_eval(line)) for line in data.splitlines() if line]

def main():
    with open("input/input.txt", "r") as f:
        data = f.read()
        all_packets = get_packets(data)
        data1 = [parse(line) for line in data.split("\n\n")]

    ordered_pairs_sum = 0
    for i, packet in enumerate(data1, start=1):
        left, right = packet
        if Packet(left) < Packet(right):
            ordered_pairs_sum += i

    print(f"Part 1: Sum of indices of ordered pairs : {ordered_pairs_sum}")

    div1 = Packet([[2]])
    div2 = Packet([[6]])

    all_packets.append(div1)
    all_packets.append(div2)

    sorted_packets = sorted(all_packets)

    i1, i2 = sorted_packets.index(div1) + 1, sorted_packets.index(div2) + 1

    print(f"Part 2: Decoder Key : {i1 * i2}")




if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds")


