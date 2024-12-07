from itertools import cycle
from typing import Literal

from profile import timer

from files import get_resource_path

DIRECTIONS = [
    (-1, 0),  # North
    (0, 1),  # East
    (1, 0),  # South
    (0, -1),  # West
]


def day6_part1() -> int:
    map: list[list[Literal[".", "#", "^"]]] = [
        list(line) for line in get_resource_path("day6.txt").read_text().splitlines()
    ]

    # Find the guard's initial position.
    for row_index, row in enumerate(map):
        for col_index, col in enumerate(row):
            if map[row_index][col_index] == "^":
                guard_position = (row_index, col_index)
                break

    # Move the guard according to the instructions.
    current_row, current_col = guard_position
    directions = cycle(DIRECTIONS)
    direction = next(directions)

    visited: set[tuple[int, int]] = set()
    while True:
        next_row = current_row + direction[0]
        next_col = current_col + direction[1]

        # If the next position is out of bounds, we're done..
        if not (0 <= next_row < len(map) and 0 <= next_col < len(map[0])):
            break

        if map[next_row][next_col] == "#":
            # If the next position is a wall, turn right.
            direction = next(directions)
        else:
            # Otherwise, move forward.
            current_row, current_col = next_row, next_col
            visited.add((current_row, current_col))

    return len(visited)


def day6_part2() -> int:
    # We can be sure a loop is occuring if guard bumps into the same obstacle twice.

    map: list[list[Literal[".", "#", "^"]]] = [
        list(line) for line in get_resource_path("day6.txt").read_text().splitlines()
    ]

    # Locations we'll try adding obstacles at.
    extra_obstacles: list[tuple[int, int]] = []

    # Find the guard's initial position.
    for row_index, row in enumerate(map):
        for col_index, col in enumerate(row):
            if map[row_index][col_index] == "^":
                guard_position = (row_index, col_index)
            elif map[row_index][col_index] == ".":
                extra_obstacles.append((row_index, col_index))

    loops_encountered = 0
    for extra_obstacle in extra_obstacles:
        # Move the guard according to the instructions.
        current_row, current_col = guard_position
        directions = cycle(DIRECTIONS)
        direction = next(directions)

        # A set of tuples of the form (obstacle, direction) indicating the obstacle and
        # direction the guard was facing when they bumped into it.
        # If we bump into the same obstacle twice from the same direction, we've hit a loop.
        collisions: set[tuple[tuple[int, int], tuple[int, int]]] = set()
        while True:
            next_row = current_row + direction[0]
            next_col = current_col + direction[1]

            # If the next position is out of bounds, we're done for this obstacle placement.
            if not (0 <= next_row < len(map) and 0 <= next_col < len(map[0])):
                break

            if map[next_row][next_col] == "#" or (next_row, next_col) == extra_obstacle:
                # If the next position is an obstacle, turn right.
                obstacle = (next_row, next_col)
                collision = (obstacle, direction)
                if collision in collisions:
                    loops_encountered += 1
                    break
                collisions.add(collision)
                direction = next(directions)
            else:
                # Otherwise, move forward.
                current_row, current_col = next_row, next_col

    return loops_encountered


if __name__ == "__main__":
    with timer("Day 6 Part 1"):
        print(day6_part1())
    with timer("Day 6 Part 2"):
        print(day6_part2())
