from collections import deque
from files import get_resource_path
from rich import print


def part1(input: str) -> int:
    lines = input.splitlines()
    grid: list[list[int]] = [list(map(int, line)) for line in lines]
    num_rows, num_cols = len(grid), len(grid[0])
    total_score = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 0:
                peaks: set[tuple[int, int]] = set()
                queue: deque[tuple[int, int]] = deque([(row, col)])

                while queue:
                    visit_row, visit_col = queue.popleft()
                    value = grid[visit_row][visit_col]

                    # Visit any adjacent cells that are 1 higher than the current cell.
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        r, c = visit_row + dr, visit_col + dc
                        if 0 <= r < num_rows and 0 <= c < num_cols:
                            if grid[r][c] == value + 1:
                                if grid[r][c] == 9 and (r, c) not in peaks:
                                    total_score += 1
                                    peaks.add((r, c))
                                else:
                                    queue.append((r, c))

    return total_score


def part2(input: str) -> int:
    lines = input.splitlines()
    grid: list[list[int]] = [list(map(int, line)) for line in lines]
    num_rows, num_cols = len(grid), len(grid[0])
    total_score = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 0:
                queue: deque[tuple[int, int]] = deque([(row, col)])

                while queue:
                    visit_row, visit_col = queue.popleft()
                    value = grid[visit_row][visit_col]

                    # Visit any adjacent cells that are 1 higher than the current cell.
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        r, c = visit_row + dr, visit_col + dc
                        if 0 <= r < num_rows and 0 <= c < num_cols:
                            if grid[r][c] == value + 1:
                                if grid[r][c] == 9:
                                    total_score += 1
                                else:
                                    queue.append((r, c))

    return total_score


def main():
    input = get_resource_path("day10.txt").read_text()
    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
