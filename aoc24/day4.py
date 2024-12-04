from collections import Counter, deque
from files import get_resource_path

SEARCH_DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


def find_word(word: str) -> int:
    # Find all occurrences of letter "x", and search in all the required directions.
    lines = get_resource_path("day4.txt").read_text().splitlines()
    grid = [list(line) for line in lines]
    found_count = 0
    for start_row, line in enumerate(grid):
        for start_column, char in enumerate(line):
            for row_delta, column_delta in SEARCH_DIRECTIONS:
                # Search in all directions. Our goal is to empty the deque, by popping
                # off characters from the deque that match the characters in the grid.
                row, column = start_row, start_column
                target = deque(word)
                while target:
                    expected_char = target[0]
                    in_bounds = 0 <= row < len(grid) and 0 <= column < len(line)
                    if not in_bounds:
                        break
                    if grid[row][column] == expected_char:
                        target.popleft()
                    else:
                        break
                    row, column = row + row_delta, column + column_delta

                if not target:
                    found_count += 1

    return found_count


def find_xmas_star_shape() -> int:
    lines = get_resource_path("day4.txt").read_text().splitlines()
    grid = [list(line) for line in lines]
    stars_found = 0
    expected_counts = Counter(M=2, S=2)
    for row in range(1, len(grid) - 1):
        for column in range(1, len(grid[row]) - 1):
            if grid[row][column] == "A":
                top_left = grid[row - 1][column - 1]
                top_right = grid[row - 1][column + 1]
                bot_left = grid[row + 1][column - 1]
                bot_right = grid[row + 1][column + 1]
                counts = Counter([top_left, top_right, bot_left, bot_right])
                if counts == expected_counts and top_left != bot_right:
                    stars_found += 1

    return stars_found


if __name__ == "__main__":
    print("Part 1 (counting XMAS):")
    print(find_word("XMAS"))

    print("Part 2 (counting MAS written in star shape):")
    print(find_xmas_star_shape())
