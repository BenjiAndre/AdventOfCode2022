import time

def main():
    with open("input/input.txt", "r") as f:
        data = f.read()

    stream_1, index_1 = process_stream(data, 4)
    stream_2, index_2 = process_stream(data, 14)

    print(f"Part 1: {stream_1} at index {index_1}")
    print(f"Part 2: {stream_2} at index {index_2}")


def process_stream(data: str, distinct_chars: int) -> tuple:
    """ Process a str of data
    Report char position when the last distinct_chars chars are all different

    Returns: tuple: (stream, position)
    """

    stream = [char for char in data[:distinct_chars]]

    for i, char in enumerate(data[distinct_chars:], start=distinct_chars):
        if len(set(stream)) == distinct_chars: # If all chars are different
            break

        stream.pop(0)
        stream.append(char)

    return stream, i


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2 - t1:0.4f} seconds")
