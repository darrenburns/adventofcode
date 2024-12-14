from collections import Counter
import functools
from profile import timer
from files import get_resource_path
from rich import print


@functools.lru_cache(maxsize=1000000)
def get_stones(stone: int) -> list[int]:
    match stone:
        case 0:
            return [1]
        case _ if len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            len_stone_string = len(stone_string)
            left_digits = stone_string[: len_stone_string // 2]
            right_digits = stone_string[len_stone_string // 2 :]
            return [int(left_digits), int(right_digits)]
        case _:
            return [stone * 2024]


@timer("Day 11 Part 1")
def part1(stones: list[int]) -> int:
    for blink in range(25):  # Blink 25 times
        new_stones: list[int] = []
        for i, stone in enumerate(stones):
            new_stones.extend(get_stones(stone))
        stones = new_stones
    return len(stones)


def blink(stones: Counter[int, int]) -> Counter[int, int]:
    """Transform the stone counts by blinking once."""
    new_stones: Counter[int, int] = Counter()
    for stone, count in stones.items():
        match stone:
            case 0:  # All 0s turn into 1s.
                new_stones[1] += count
            case _ if len(str(stone)) % 2 == 0:  # Split into 2 stones.
                new_stones[int(str(stone)[: len(str(stone)) // 2])] += count
                new_stones[int(str(stone)[len(str(stone)) // 2 :])] += count
            case _:  # Multiply by 2024.
                new_stones[stone * 2024] += count
    return new_stones


@timer("Day 11 Part 2")
def part2(stones: list[int]) -> int:
    # Order of stones is not important and so we shouldn't maintain the full list of stones.
    # We just need to keep track of the counts. We can modify the counts after each blink.
    counts: Counter[int, int] = Counter(stones)
    for _ in range(75):
        counts = blink(counts)
    return sum(counts.values())


if __name__ == "__main__":
    input = get_resource_path("day11.txt").read_text()
    stones = list(map(int, input.split(" ")))
    print(part1(stones))
    print(part2(stones))
