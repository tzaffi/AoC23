import re

DIG_CHARS = "0123456789"
DIG_REX = r"^(one|two|three|four|five|six|seven|eight|nine|zero)"


def s2i(s):
    match s:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case "zero":
            return 0
    raise ValueError(f"Invalid digit: {s}")


def simple(line):
    d1 = d2 = 0
    for i, c in enumerate(line):
        if c in DIG_CHARS:
            d1 = int(c)
            break

    for j in range(len(line) - 1, i - 1, -1):
        if (c := line[j]) in DIG_CHARS:
            d2 = int(c)
            break

    return 10 * d1 + d2


def complex(line):
    d1 = d2 = 0
    for i, c in enumerate(line):
        if c in DIG_CHARS:
            d1 = int(c)
            break
        if m := re.match(DIG_REX, line[i:]):
            d1 = s2i(m.group(1))
            break

    for j in range(len(line) - 1, i - 1, -1):
        if (c := line[j]) in DIG_CHARS:
            d2 = int(c)
            break
        if m := re.match(DIG_REX, line[j:]):
            d2 = s2i(m.group(1))
            break

    return 10 * d1 + d2


def t1(text):
    return sum(simple(ln) for ln in text.splitlines())


def t2(text):
    return sum(complex(ln) for ln in text.splitlines())


if __name__ == "__main__":
    with open("trebuchet_in.txt") as f:
        print(t1(f.read()))

    with open("trebuchet_in.txt") as f:
        print(t2(f.read()))
