from .closest_planets import Planet, closest_planets


def list_iterator(xs):
    for x in xs:
        yield x


def test_closest_planets():
    planets = [
        Planet(2, 3, 4),
        Planet(1, 2, 3),
        Planet(3, 4, 5),
        Planet(4, 5, 6),
        Planet(0, 0, 0),
    ]
    assert [planets[4], planets[1]] == closest_planets(list_iterator(planets), 2)

    assert [] == closest_planets(list_iterator([]), 2)

    assert [planets[4], planets[1], planets[0]] == closest_planets(
        list_iterator(planets), 3
    )

    assert [planets[4], planets[1], planets[0], planets[2]] == closest_planets(
        list_iterator(planets), 4
    )
