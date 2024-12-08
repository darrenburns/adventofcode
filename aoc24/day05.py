from collections import defaultdict
from functools import cmp_to_key
from profile import timer
from files import get_resource_path


@timer("Day 5 Part 1")
def day5_part1():
    data = iter(get_resource_path("day5.txt").read_text().splitlines())
    order_rules: dict[int, set[int]] = defaultdict(set)
    for line in data:
        if not line.strip():
            break
        left, right = line.split("|")  # Left must come before right.
        order_rules[int(left)].add(int(right))

    for line in data:
        seen_this_line: set[int] = set()
        numbers = [int(number) for number in line.split(",")]
        rule_holds = True
        for number in numbers:
            # Check that this number satisfies the order rules when in the context
            # of all numbers seen thus far on this line.
            for previous_number in seen_this_line:
                if previous_number in order_rules[number]:
                    # The order rule is violated.
                    rule_holds = False
                    break

            if not rule_holds:
                break

            seen_this_line.add(number)

        if rule_holds:
            middle_number = numbers[len(numbers) // 2]
            yield middle_number


@timer("Day 5 Part 2")
def day5_part2():
    data = iter(get_resource_path("day5.txt").read_text().splitlines())
    order_rules: dict[int, set[int]] = defaultdict(set)
    for line in data:
        if not line.strip():
            break
        left, right = line.split("|")  # Left must come before right.
        order_rules[int(left)].add(int(right))

    total_score = 0
    for line in data:
        seen_this_line: set[int] = set()
        numbers = [int(number) for number in line.split(",")]
        fixed = False
        for number in numbers:
            # Check that this number satisfies the order rules when in the context
            # of all numbers seen thus far on this line.
            for previous_number in seen_this_line:
                if previous_number in order_rules[number]:
                    sorted_numbers = fix_order(numbers, order_rules)
                    total_score += sorted_numbers[len(sorted_numbers) // 2]
                    fixed = True
                    break

            if fixed:
                break

            seen_this_line.add(number)

    return total_score


def fix_order(numbers: list[int], order_rules: dict[int, set[int]]) -> list[int]:
    """Given a list of numbers and a set of order rules, return a list of numbers
    that satisfies the order rules."""
    fixed_numbers: list[int] = numbers.copy()

    def comparison_function(left: int, right: int) -> int:
        if left in order_rules:
            if right in order_rules[left]:
                return -1
            else:
                return 1
        return 0

    fixed_numbers.sort(key=cmp_to_key(comparison_function))
    return fixed_numbers


if __name__ == "__main__":
    print(sum(day5_part1()))
    print(day5_part2())
