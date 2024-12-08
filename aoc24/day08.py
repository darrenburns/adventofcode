from collections import defaultdict
from profile import timer
from files import get_resource_path
from rich import print


@timer("Day 8 Part 1")
def part1():
    data = get_resource_path("day8.txt").read_text()

    grid = [list(line) for line in data.splitlines()]

    antinodes: set[tuple[int, int]] = set()

    # Mapping frequencies to a list of coordinates that have that frequency.
    antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)

    def valid_location(row_index: int, col_index: int) -> bool:
        return 0 <= row_index < len(grid) and 0 <= col_index < len(grid[0])

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell.isalnum():
                # Check prior discoveries of this frequency.
                if cell in antennas:
                    for other_row, other_col in antennas[cell]:
                        row_offset, col_offset = (
                            row_index - other_row,
                            col_index - other_col,
                        )
                        # Apply this offset to the current value
                        first_antinode = (
                            row_index + row_offset,
                            col_index + col_offset,
                        )
                        if valid_location(first_antinode[0], first_antinode[1]):
                            antinodes.add(first_antinode)

                        second_antinode = (
                            other_row - row_offset,
                            other_col - col_offset,
                        )
                        if valid_location(second_antinode[0], second_antinode[1]):
                            antinodes.add(second_antinode)

                antennas[cell].append((row_index, col_index))

    return len(antinodes)


@timer("Day 8 Part 2")
def part2():
    data = get_resource_path("day8.txt").read_text()

    grid = [list(line) for line in data.splitlines()]

    antinodes: set[tuple[int, int]] = set()

    # Mapping frequencies to a list of coordinates that have that frequency.
    antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)

    def valid_location(row_index: int, col_index: int) -> bool:
        return 0 <= row_index < len(grid) and 0 <= col_index < len(grid[0])

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell.isalnum():
                # Check prior discoveries of this frequency.
                if cell in antennas:
                    for other_row, other_col in antennas[cell]:
                        row_offset, col_offset = (
                            row_index - other_row,
                            col_index - other_col,
                        )
                        antinodes.add((row_index, col_index))
                        # Apply this offset to the current value
                        current_row, current_col = (
                            row_index + row_offset,
                            col_index + col_offset,
                        )
                        while valid_location(current_row, current_col):
                            antinodes.add((current_row, current_col))
                            current_row += row_offset
                            current_col += col_offset

                        antinodes.add((other_row, other_col))
                        current_row, current_col = (
                            other_row - row_offset,
                            other_col - col_offset,
                        )
                        while valid_location(current_row, current_col):
                            antinodes.add((current_row, current_col))
                            current_row -= row_offset
                            current_col -= col_offset

                antennas[cell].append((row_index, col_index))

    return len(antinodes)


if __name__ == "__main__":
    print(part1())
    print(part2())
