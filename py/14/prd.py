"""
prd == Parabolic Reflector Dishes
"""

from copy import deepcopy
from enum import Enum


class Direction(Enum):
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3


class RockGrid:
    def __init__(self, grid_text: str):
        self.grid = [list(row) for row in grid_text.splitlines()]
        self.shape = (len(self.grid), len(self.grid[0]))

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)

    def __getitem__(self, row):
        return deepcopy(self.grid[row])

    def __eq__(self, other):
        if not isinstance(other, RockGrid):
            return False
        return str(self) == str(other)

    @staticmethod
    def condense(a: list) -> None:
        """Push all movable rocks to the right as much as possible"""
        right = len(a) - 1
        left = right - 1
        while left >= 0:
            while a[right] != "." and left >= 0:
                right -= 1
                left = right - 1
            # WLOG a[right] == "." and left == right-1
            while left >= 0 and a[left] != "#":
                if a[left] == "O":
                    a[left], a[right] = a[right], a[left]
                    right -= 1
                left -= 1
            if left >= 0:  # a[left] == "#"
                right = left - 1
                left = right - 1

    def gravitate(self, direction: Direction) -> None:
        # is_rc = "is row condensation"
        is_rc = direction in (Direction.EAST, Direction.WEST)

        # is_right = "is rightward"
        is_right = direction in (Direction.EAST, Direction.SOUTH)

        range_size = self.shape[1 if is_rc else 0]
        iter_range = range(range_size) if is_right else range(range_size - 1, -1, -1)

        def get_ith(i):
            return [self.grid[i][j] if is_rc else self.grid[j][i] for j in iter_range]

        cond_range = range(self.shape[0 if is_rc else 1])
        for i in cond_range:
            a = get_ith(i)
            self.condense(a)
            if not is_right:
                a.reverse()
            for j in iter_range:
                if is_rc:
                    self.grid[i][j] = a[j]
                else:
                    self.grid[j][i] = a[j]

    def load(self) -> int:
        return sum(
            (self.shape[0] - i) * row.count("O") for i, row in enumerate(self.grid)
        )

    def cycle(self) -> None:
        self.gravitate(Direction.NORTH)
        self.gravitate(Direction.WEST)
        self.gravitate(Direction.SOUTH)
        self.gravitate(Direction.EAST)

    def _fixpoint_impl(self) -> tuple[int, int]:
        """
        As hash(x) is a 64 bit number, and the AoC
        problem states that we only need consider < 2^30
        states, the chance of collision is negligible.
        """
        i = 0
        seen = {hash(str(self)): i}
        while True:
            i += 1
            self.cycle()
            h = hash(str(self))
            if h in seen:
                return seen[h], i - seen[h]
            seen[h] = i

    @classmethod
    def find_fixpoint(cls, grid_text: str) -> tuple[int, int]:
        return cls(grid_text)._fixpoint_impl()

    def extrapolate_spin(self, n: int) -> None:
        fixpoint, period = self.find_fixpoint(str(self))

        for _ in range(min(fixpoint, n)):
            self.cycle()

        if n <= fixpoint:
            return

        cycles = (n - fixpoint) % period
        for _ in range(cycles):
            self.cycle()


if __name__ == "__main__":
    with open("14/input.txt") as f:
        grid_str = f.read()

    grid = RockGrid(grid_str)
    grid.gravitate(Direction.NORTH)
    print(grid.load())

    print(RockGrid.find_fixpoint(grid_str))
    grid = RockGrid(grid_str)
    grid.extrapolate_spin(1_000_000_000)
    print(grid.load())
