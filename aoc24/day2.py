"""https://adventofcode.com/2024/day/2"""

from files import get_resource_path


def is_safe_report(values: list[int]) -> bool:
    """Determine if a report is safe."""
    all_increasing, all_decreasing, adjacent_limit = True, True, True
    previous_index, index = 0, 1
    while index < len(values):
        current_value = values[index]
        previous_value = values[previous_index]

        # Set any of the flags to False if the required conditions are not met.
        all_increasing = all_increasing and current_value > previous_value
        all_decreasing = all_decreasing and current_value < previous_value
        adjacent_limit = (
            adjacent_limit and 1 <= abs(current_value - previous_value) <= 3
        )

        index += 1
        previous_index = index - 1

    return (all_increasing or all_decreasing) and adjacent_limit


def count_safe_reports() -> int:
    """
    Part 2: Count the number of safe reports.
    """
    lines = get_resource_path("day2.txt").read_text().splitlines()
    safe_count = 0
    for line in lines:
        values = [int(value) for value in line.split()]
        safe_count += is_safe_report(values)
    return safe_count


if __name__ == "__main__":
    print(count_safe_reports())
