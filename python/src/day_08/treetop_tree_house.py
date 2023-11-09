import time
from dataclasses import dataclass

@dataclass(frozen=True)
class Tree():
    """ Tree class, has coordinates of it's place in the forest (x,y)"""
    x: int
    y: int

class Forest():
    
    def __init__(self, data: list) -> None:
        """ Expects data as a list of tree rows :
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], ...]"""
        self.rows = data
        self.cols = list(zip(*self.rows))
        self._width = len(self.cols)
        self._height = len(self.rows)
        self.size = self._width * self._height

    def height_of_tree(self, tree: Tree) -> int:
        return self.rows[tree.y][tree.x]

    def is_visible(self, tree: Tree) -> int:
        """ Check if a tree is visible from any edge of the forest"""

        if tree.x == 0 or tree.x == self._width - 1:
            return True
        if tree.y == 0 or tree.y == self._height - 1:
            return True

        height = self.height_of_tree(tree)

        if height > max(self.rows[tree.y][0:tree.x]): return True
        if height > max(self.rows[tree.y][tree.x + 1:]): return True
        if height > max(self.cols[tree.x][0:tree.y]): return True
        if height > max(self.cols[tree.x][tree.y + 1:]): return True

        return False

    def get_visible_trees(self) -> set[Tree]:
        return { Tree(x, y) for x in range(self._height)
                            for y in range(self._width)
                            if self.is_visible(Tree(x, y))}

    def best_scenic_score(self) -> int:
        """ Return the best scenic score in the forest"""
        best = 0
        for y in range(self._width):
            for x in range(self._height):
                tree = Tree(x, y)
                score = self.get_tree_scenic_score(tree)
                if score > best:
                    best = score

        return best

    def get_tree_scenic_score(self, tree: Tree) -> int:
        """ Returns the scenic score of a given tree in the forest"""

        height = self.height_of_tree(tree)

        right = (x for x in self.rows[tree.y][tree.x+1:])
        bottom = (y for y in self.cols[tree.x][tree.y+1:])
        left = (x for x in reversed(self.rows[tree.y][0:tree.x]))
        top = (x for x in reversed(self.cols[tree.x][0:tree.y]))

        res = 1
        for direction in (right, bottom, left, top):
            visible_trees = 0
            for t_height in direction:
                if t_height < height:
                    visible_trees += 1
                else:
                    visible_trees += 1
                    break
            res *= visible_trees

        return res



        


def main():
    with open("input/input.txt", "r") as f:
        data = f.read().splitlines()

    forest = Forest(data)
    visible = forest.get_visible_trees()
    print(f"Part 1: Number of visible trees : {len(visible)}")
    scenic_score = forest.best_scenic_score()
    print(f"Part 2: Best scenic score of the forest : {scenic_score}")

    

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time : {t2-t1:0.4f} seconds")
