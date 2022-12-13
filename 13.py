import sys

fav_num = int(sys.stdin.readline())
step_counts: dict[tuple[int, int], int] = {(1, 1): 0}


def main():
    spread(1, 1)

    print("Part 1:", step_counts[(31, 39)])

    at_most_50 = 0
    for count in step_counts.values():
        if count <= 50:
            at_most_50 += 1
    print("Part 2:", at_most_50)


def spread(x: int, y: int):
    current_step = step_counts[(x, y)]

    if x > 0:
        walk(current_step, x - 1, y)

    walk(current_step, x + 1, y)

    if y > 0:
        walk(current_step, x, y - 1)

    walk(current_step, x, y + 1)


def walk(current_step: int, x: int, y: int):
    if is_wall(x, y):
        return

    if (x, y) not in step_counts or step_counts[(x, y)] > current_step + 1:
        step_counts[(x, y)] = current_step + 1
        spread(x, y)


def is_wall(x: int, y: int) -> bool:
    val = bin(x * x + 3 * x + 2 * x * y + y + y * y + fav_num)
    ones = 0
    for c in val:
        if c == "1":
            ones += 1

    return ones % 2 == 1


if __name__ == "__main__":
    main()
