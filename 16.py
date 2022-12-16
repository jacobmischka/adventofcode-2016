import sys


def main():
    input = sys.stdin.readline().strip()

    print(f"Part 1: {gen_checksum(fill_disk(input, 272))}")
    print(f"Part 2 {gen_checksum(fill_disk(input, 35651584))}")


def fill_disk(input: str, disk_size: int) -> str:
    while len(input) < disk_size:
        input = (
            input
            + "0"
            + "".join(["1" if c == "0" else "0" for c in reversed(list(input))])
        )

    return input[:disk_size]


def gen_checksum(input: str) -> str:
    while len(input) % 2 == 0:
        checksum = []
        for i in range(0, len(input), 2):
            left = input[i]
            right = input[i + 1]
            checksum.append("1" if left == right else "0")
        input = "".join(checksum)

    return input


if __name__ == "__main__":
    main()
