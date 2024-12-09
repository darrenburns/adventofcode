from collections import deque
from files import get_resource_path
from profile import timer


@timer("Part 1")
def part1(input: str) -> int:
    reversed_blocks: deque[str] = deque(reversed(input))
    file_id = 0
    for i in range(0, len(reversed_blocks) - 1, 2):
        block = int(reversed_blocks[i])
        free_spaces = int(reversed_blocks[i + 1])
        this_block = [file_id] * block + []

        file_id += 1


@timer("Part 2")
def part2(input: str) -> int:
    pass


if __name__ == "__main__":
    input = get_resource_path("day9.txt").read_text()
    print(part1(input))
    print(part2(input))
