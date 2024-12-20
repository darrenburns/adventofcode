import re
from profile import timer
from files import get_resource_path

FIND_DOS = re.compile(r"do\(\)")
FIND_DONTS = re.compile(r"don't\(\)")
FIND_MULS = re.compile(r"mul\((\d+),(\d+)\)")


@timer("Day 3 Part 1")
def part1():
    data = get_resource_path("day3.txt").read_text()
    mul_calls = FIND_MULS.findall(data)
    return sum(int(a) * int(b) for a, b in mul_calls)


@timer("Day 3 Part 2")
def part2():
    data = get_resource_path("day3.txt").read_text()
    mul_calls = list(FIND_MULS.finditer(data))
    dos = list(FIND_DOS.finditer(data))
    donts = list(FIND_DONTS.finditer(data))

    matches = sorted(mul_calls + dos + donts, key=lambda m: m.start())
    enabled = True
    total = 0
    for match in matches:
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else:
            if enabled:
                total += int(match.group(1)) * int(match.group(2))

    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
