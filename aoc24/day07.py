from files import get_resource_path


def day7_part1() -> int:
    data = get_resource_path("day7.txt").read_text().splitlines()
    total = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = [int(number.strip()) for number in numbers.split()]

        def hits_target(index: int, prefix: int) -> bool:
            # For each value, consider both + and * with all the possible prefixes
            # that came before it (recursively generated).
            if index == len(numbers) - 1:
                return (
                    prefix + numbers[index] == target
                    or prefix * numbers[index] == target
                )
            plus_hit = hits_target(index + 1, prefix + numbers[index])
            times_hit = hits_target(index + 1, prefix * numbers[index])
            return plus_hit or times_hit

        if hits_target(0, 0):
            total += target

    return total


def concat_numbers(left: int, right: int) -> int:
    return int(str(left) + str(right))


def day7_part2() -> int:
    data = get_resource_path("day7.txt").read_text().splitlines()
    total = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = [int(number.strip()) for number in numbers.split()]

        def hits_target(index: int, prefix: int) -> bool:
            # For each value, consider both + and * with all the possible prefixes
            # that came before it (recursively generated).
            if index == len(numbers) - 1:
                return (
                    prefix + numbers[index] == target
                    or prefix * numbers[index] == target
                    or concat_numbers(prefix, numbers[index]) == target
                )
            plus_hit = hits_target(index + 1, prefix + numbers[index])
            times_hit = hits_target(index + 1, prefix * numbers[index])
            concat_hit = hits_target(index + 1, concat_numbers(prefix, numbers[index]))
            return plus_hit or times_hit or concat_hit

        if hits_target(0, 0):
            total += target

    return total


if __name__ == "__main__":
    print(day7_part1())
    print(day7_part2())
