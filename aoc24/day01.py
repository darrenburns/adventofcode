"""https://adventofcode.com/2024/day/1"""

from collections import Counter
import heapq
from profile import timer
from files import get_resource_path


@timer("Day 1 Part 1")
def compute_total_distance() -> int:
    """
    Part 1: Compute the total distance between the left and right lists.

    We're using heaps here since they can be built in O(n) time.
    If we were to sort the lists after, it would be O(nlogn) time.
    """
    lines = get_resource_path("day1.txt").read_text().splitlines()
    left_values: list[int] = []
    right_values: list[int] = []
    for line in lines:
        left, right = line.split("   ")
        heapq.heappush(left_values, int(left))
        heapq.heappush(right_values, int(right))

    total_distance = 0
    while left_values and right_values:
        left = heapq.heappop(left_values)
        right = heapq.heappop(right_values)
        total_distance += abs(left - right)

    return total_distance


@timer("Day 1 Part 2")
def compute_similarity_score() -> int:
    """
    Part 2: Compute the similarity score between the left and right lists.

    A variation on part 1, but this time we can't just pop once from each list.
    """
    lines = get_resource_path("day1.txt").read_text().splitlines()

    left_values: list[int] = []
    right_values: list[int] = []
    for line in lines:
        left, right = line.split("   ")
        left_values.append(int(left))
        right_values.append(int(right))

    right_counts = Counter(right_values)
    similarity_score = 0
    for left_value in left_values:
        similarity_score += left_value * right_counts[left_value]

    return similarity_score


if __name__ == "__main__":
    distance = compute_total_distance()
    print(distance)

    similarity_score = compute_similarity_score()
    print(similarity_score)
