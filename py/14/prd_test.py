from prd import Direction, RockGrid

fixture = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

north = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""

cycle_1 = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""


cycle_2 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O"""


cycle_3 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O"""


def test_init():
    """Test roll()."""
    rg = RockGrid(fixture)
    assert (10, 10) == rg.shape
    assert fixture == str(rg)
    assert ["O", "O", ".", "#", "O", ".", ".", ".", ".", "O"] == rg[3]


def test_condense():
    grid = RockGrid(fixture).grid
    row_3 = grid[3]
    assert ["O", "O", ".", "#", "O", ".", ".", ".", ".", "O"] == row_3

    col_3 = [grid[i][3] for i in range(10)]
    assert [".", "O", ".", "#", ".", ".", ".", ".", ".", "."] == col_3

    RockGrid.condense(row_3)
    assert [".", "O", "O", "#", ".", ".", ".", ".", "O", "O"] == row_3

    RockGrid.condense(col_3)
    assert [".", ".", "O", "#", ".", ".", ".", ".", ".", "."] == col_3


def test_gravitate():
    rg = RockGrid(fixture)
    rg.gravitate(Direction.NORTH)
    assert north == str(rg)


def test_load():
    rg = RockGrid(north)
    assert 136 == rg.load()


def test_cycle():
    rg = RockGrid(fixture)

    rg.cycle()
    assert cycle_1 == str(rg)

    rg.cycle()
    assert cycle_2 == str(rg)

    rg.cycle()
    assert cycle_3 == str(rg)


def test_find_fixpoint():
    assert (3, 7) == RockGrid.find_fixpoint(fixture)

    rg = RockGrid(fixture)
    for _ in range(3):
        rg.cycle()
    state_3 = str(rg)

    for _ in range(7):
        rg.cycle()
    state_10 = str(rg)

    assert state_3 == state_10


def test_extrapolate_spin():
    def spin(rg, n):
        for _ in range(n):
            rg.cycle()

    for n in range(11):
        rg1 = RockGrid(fixture)
        rg2 = RockGrid(fixture)

        spin(rg1, n)
        rg2.extrapolate_spin(n)
        assert rg1 == rg2
