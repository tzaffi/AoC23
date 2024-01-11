from math import prod


class Game:
    def __init__(self, game_str):
        pre, post = game_str.strip().split(":")
        self.number = int(pre.split(" ")[-1])

        def get_rev(s):
            return {
                k: int(v) for v, k in (term.strip().split(" ") for term in s.split(","))
            }

        self.subsets = [
            ((r := get_rev(rev)).get("red", 0), r.get("green", 0), r.get("blue", 0))
            for rev in post.strip().split(";")
        ]


class Games:
    def __init__(self, games_str):
        self.games: list[Game] = [Game(line) for line in games_str.splitlines()]

    def possible(self, threshold: tuple[int]) -> list[int]:
        return [
            g.number
            for g in self.games
            if all(all(r[i] <= c for i, c in enumerate(threshold)) for r in g.subsets)
        ]

    def sum_of_power(self) -> int:
        # res = 0
        # # for g in self.games:
        # #     # new_power = 1
        # #     # print(list(zip(*g.subsets)))
        # #     # Take logarithms, equivalent to sum
        # #     # for x in [max(color_block) for color_block in zip(*g.subsets)]:
        # #     #     new_power *= x
        # #     res += prod(max(color_block) for color_block in zip(*g.subsets))
        # return res
        return sum(
            prod(max(color_block) for color_block in zip(*g.subsets))
            for g in self.games
        )

    def id_sum(self, threshold: tuple[int]) -> int:
        return sum(self.possible(threshold))


if __name__ == "__main__":
    # with open("conundrum_in.txt") as f:
    #     print(Games(f.read()).id_sum((12, 13, 14)))
    with open("conundrum_in.txt") as f:
        print(Games(f.read()).sum_of_power())
