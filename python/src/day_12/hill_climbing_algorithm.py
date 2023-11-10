import time
from queue import Queue

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_pos(data, val):
    """ Finds the position of the value val in data"""
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if data[i][j] == val:
                return i, j

def find_all_pos(data, val):
    """ Finds the position of all the values val in data"""
    positions = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if data[i][j] == val:
                positions.append((i,j))
    return positions


def valid_direction(data, pos, length):
    """ Finds the valid directions to go from position pos in data of length i*j"""
    valid = []
    pos_data = ord(data[pos[0]][pos[1]])
    for direction in DIRECTIONS:
        cur = pos[0] + direction[0], pos[1] + direction[1]
        if 0 <= cur[0] < length[0] and 0 <= cur[1] < length[1]:
            cur_data = ord(data[cur[0]][cur[1]])
            if cur_data <= pos_data + 1 :
                valid.append(cur)
    return valid

def bfs(data, start, end):
    data_len = len(data), len(data[0])
    queue = Queue()
    queue.put((start[0], start[1], 0))
    visited = [[False for _ in range(data_len[1])] for _ in range(data_len[0])]
    data[start[0]][start[1]] = 'a'
    data[end[0]][end[1]] = 'z'

    while queue.qsize() > 0:
        # Get the next node to visit and return if it's the end
        i, j, length = queue.get()
        if (i, j) == end:
            return length
        
        # Visit the node
        visited[i][j] = True
        length += 1
        # See what node to visit next
        for x,y in valid_direction(data, (i,j), data_len):
            if not visited[x][y] and (x,y) not in [(l[0],l[1]) for l in list(queue.queue)]:
                queue.put((x, y, length)) 

    return 530

def main():
    with open("input/input.txt", "r") as f:
        data = [list(line) for line in f.read().splitlines()]

    start = find_pos(data, 'S')
    end = find_pos(data, 'E')

    length = bfs(data, start, end)
    print(f"Part 1 : Fewest possible steps : {length}")

    positions = find_all_pos(data, 'a')
    all_length = [bfs(data, (i,j), end) for i,j in positions]
    print(f"Part 2 : Fewest possible tests puissance 9000 : {min(all_length)}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
