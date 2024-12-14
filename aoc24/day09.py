from collections import deque
from files import get_resource_path
from profile import timer


def expand_blocks(blocks: str) -> str:
    left, right = 0, 1
    expanded: list[str] = []
    file_id = 0
    while left < len(blocks):
        block_count, free_count = (
            int(blocks[left]),
            int(blocks[right]) if right < len(blocks) else 0,
        )
        expanded.extend([str(file_id)] * block_count + ["."] * free_count)
        file_id += 1
        left += 2
        right += 2

    return expanded


@timer("Part 1")
def part1(input: str) -> int:
    expanded: deque[str] = deque(expand_blocks(input))
    index, checksum = 0, 0
    result: deque[str] = deque()
    while expanded:
        block = expanded.popleft()
        if block == ".":
            if not expanded:
                break
            while (block := expanded.pop()) == ".":
                pass

        result.append(block)
        checksum += index * int(block)
        index += 1

    return checksum


def get_contiguous_blocks(blocks: str) -> list[tuple[int, int]]:
    """Return a list of tuples, where the first element is the file id and the second is the block count.
    Free blocks are represented by a file ID of -1.
    """
    contiguous: list[tuple[int, int]] = []
    left, right = 0, 1
    file_id = 0
    while left < len(blocks):
        block_count, free_count = (
            int(blocks[left]),
            int(blocks[right]) if right < len(blocks) else 0,
        )
        contiguous.append((file_id, block_count))
        contiguous.append((-1, free_count))
        file_id += 1
        left += 2
        right += 2
    return contiguous


@timer("Part 2")
def part2(input: str) -> int:
    expanded: list[tuple[int, int]] = get_contiguous_blocks(input)
    right = len(expanded) - 1
    checksum = 0
    moving_id = max(expanded, key=lambda x: x[0])[0]
    while moving_id > 0:
        # Find the block we're moving.
        while (right_value := expanded[right])[0] != moving_id:
            right -= 1

        _, right_width = right_value
        moving_id -= 1

        # Find a slot for the block.
        slot_found = False
        for index, (file_id, block_width) in enumerate(expanded[:right]):
            if not (file_id != -1 or block_width < right_width):
                # The block from the right doesn't fit in this slot, or this
                # slot is not "free space".
                slot_found = True
                left = index
                break

        if slot_found:
            free_space = expanded[left]
            remaining_width = free_space[1] - right_width
            expanded[right] = (-1, right_width)  # The moved block is now free.
            expanded.insert(left, right_value)
            expanded[left + 1] = (-1, remaining_width)

    # Now do another pass to compute the checksum.
    index = 0
    for file_id, block_width in expanded:
        for index_in_block in range(block_width):
            if file_id == -1:
                continue
            checksum += (index + index_in_block) * file_id
        index += block_width

    return checksum


if __name__ == "__main__":
    input = get_resource_path("day9.txt").read_text()
    print(part1(input))
    print(part2(input))
