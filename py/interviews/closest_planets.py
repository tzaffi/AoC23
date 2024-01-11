"""
You have a sequence of planets with coordinates (x, y, z) in 3D space with
you at (0, 0, 0). Find the closest k planets to you.
"""

from dataclasses import dataclass
import heapq
from typing import Iterator


class Planet:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z
        self.norm = self._norm()

    def _norm(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def __lt__(self, other: "Planet") -> bool:
        return self.norm < other.norm


def closest_planets(planets: Iterator[Planet], k: int) -> list[Planet]:
    h = []
    for _ in range(k):
        if (p := next(planets, None)) is None:
            break

        h.append((-p.norm, p))

    heapq.heapify(h)

    while (p := next(planets, None)) is not None:
        if p < h[0][1]:
            heapq.heappushpop(h, (-p.norm, p))

    N = len(h)
    res = [None] * N
    for i in range(N - 1, -1, -1):
        res[i] = heapq.heappop(h)[1]
    return res
