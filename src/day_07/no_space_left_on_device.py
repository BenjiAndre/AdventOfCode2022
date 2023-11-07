from __future__ import annotations
import time
from dataclasses import dataclass

@dataclass(frozen=True)
class File:
    name: str
    size: int

class Directory:
    """Represents a file system directory. Has a parent directory,
    subdirectories or/and files.
    """
    def __init__(self, name: str) -> None:
        self._name = name
        self._files: list[File] = []
        self._dirs: list[Directory] = []

    @property
    def name(self):
        return self._name

    @property
    def parent_dir(self):
        return self._parent_dir

    @parent_dir.setter
    def parent_dir(self, value):
        self._parent_dir = value

    @property
    def directories(self):
        return self._dirs

    def get_directory(self, name: str) -> Directory:
        return next(dir for dir in self.directories if dir.name == name)

    def get_all_dirs(self) -> list[Directory]:
        all_dirs = []
        for directory in self.directories:
            all_dirs.extend(directory.get_all_dirs())

        all_dirs.extend(self.directories)

        return all_dirs

    @property
    def size(self):
        return sum(file.size for file in self._files) + sum(directory.size for directory in self._dirs)

    def add_file(self, file: File):
        self._files.append(file)

    def add_directory(self, directory: Directory):
        self._dirs.append(directory)
        directory._parent_dir = self


def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    root = parse(data)
    directories = root.get_all_dirs()

    small_directories = [d for d in directories if d.size <= 100000]
    print(f"Part 1: Directories with size < 100 000 : {sum(d.size for d in small_directories)}")

    current_size = 70000000 - root.size
    size_needed = 30000000 - current_size
    big_enough_dirs = [d for d in directories if d.size >= size_needed]
    smallest = min(big_enough_dirs, key=lambda x: x.size)
    print(f"Part 2: Name of directory to delete : {smallest.name}, size : {smallest.size}")


def parse(data: list[str]) -> Directory:
    root = Directory("/")
    current = root

    for line in data:
        if line.startswith("$"):
            instruction = line.split()
            command = instruction[1]
            if command == "ls":
                continue
            if command == "cd":
                argument = instruction[2]
                if argument == "..":
                    current = current.parent_dir
                elif argument != '/':
                    current = current.get_directory(argument)
                else:
                    current = root
        else:
            element = line.split()
            if element[0] == "dir":
                directory = Directory(element[1])
                current.add_directory(directory)
            else:
                file = File(element[1], size=int(element[0]))
                current.add_file(file)

    return root 

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
