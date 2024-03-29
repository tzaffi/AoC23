from trebuchet import t1, t2


def test_t1():
    eg = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert 142 == t1(eg)


def test_t2():
    eg = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert 281 == t2(eg)
