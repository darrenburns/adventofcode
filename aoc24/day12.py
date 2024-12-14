from profile import timer
from files import get_resource_path
from rich import print


@timer("Day 12 Part 1")
def part1(input: str) -> int:
    # We'll perform a recursive BFS each time we encounter a new character.
    # When checking boundaries, if we discover a different character or the
    # edge of the grid, we'll count it as a "fence". If we discover the same
    # character, we'll continue our BFS.
    grid = [list(line) for line in input.splitlines()]
    visited: set[tuple[int, int]] = set()
    fences: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    total_prices = 0

    def in_bounds(row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])

    def find_fences(row: int, col: int, original_plant: str):
        """Perform a flood fill to compute the area from the given starting point."""
        # Ensure we only account for this cell once.
        if (row, col) in visited:
            return

        visited.add((row, col))
        # Look at neighbouring cells, decide whether we should visit them.
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            target_row, target_col = row + dr, col + dc
            if (
                not in_bounds(target_row, target_col)
                or grid[target_row][target_col] != original_plant
            ):
                # If we're at a boundary,
                fences.add(tuple(sorted([(row, col), (target_row, target_col)])))
            else:
                # Otherwise, we'll continue our flood fill.
                find_fences(target_row, target_col, original_plant)

    # For each cell in the grid, flood outwards to find all connected cells of the same letter.
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if (row_index, col_index) in visited:
                continue

            prev_len_visited = len(visited)
            original_plant = grid[row_index][col_index]
            find_fences(row_index, col_index, original_plant)
            fence_count = len(fences)
            # The number of cells we visited on the find_fences call is the area.
            area = len(visited) - prev_len_visited
            total_prices += area * fence_count
            fences.clear()

    return total_prices


def part2(input: str) -> int:
    return 0


if __name__ == "__main__":
    input = get_resource_path("day12.txt").read_text()
    print(part1(input))
    print(part2(input))
