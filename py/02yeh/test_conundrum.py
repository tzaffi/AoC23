from conundrum import Game, Games

test_case = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_game_init():
    game_str = (
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    game = Game(game_str)
    assert 3 == game.number
    assert 3 == len(game.subsets)
    assert game.subsets[0] == (20, 8, 6)
    assert game.subsets[1] == (4, 13, 5)
    assert game.subsets[2] == (1, 5, 0)


def test_games_init():
    games = Games(test_case)
    assert 5 == len(games.games)
    assert [1, 2, 3, 4, 5] == [g.number for g in games.games]


def test_possible_games():
    games = Games(test_case)
    assert [1, 2, 5] == games.possible((12, 13, 14))


def test_id_sum():
    games = Games(test_case)
    assert 8 == games.id_sum((12, 13, 14))
