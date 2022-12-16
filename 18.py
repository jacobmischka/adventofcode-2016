import sys

SAFE = "."
TRAP = "^"


def main():
    input = sys.stdin.readline().strip()

    print(f"Part 1: {count_safe(input, 40)}")
    print(f"Part 2: {count_safe(input, 400000)}")


def count_safe(prev_row: str, num_rows: int) -> int:
    safe_tiles = 0
    for c in prev_row:
        if c == SAFE:
            safe_tiles += 1

    for _ in range(num_rows - 1):  # already 1 row
        new_row = ""
        for i in range(len(prev_row)):
            left = prev_row[i - 1] if i > 0 else "."
            center = prev_row[i]
            right = prev_row[i + 1] if i < len(prev_row) - 1 else "."

            tile = (
                TRAP
                if (
                    (left == TRAP and center == TRAP and right == SAFE)
                    or (center == TRAP and right == TRAP and left == SAFE)
                    or (left == TRAP and center == SAFE and right == SAFE)
                    or (left == SAFE and center == SAFE and right == TRAP)
                )
                else SAFE
            )
            if tile == SAFE:
                safe_tiles += 1

            new_row += tile
        prev_row = new_row
    return safe_tiles


if __name__ == "__main__":
    main()
