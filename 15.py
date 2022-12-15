from dataclasses import dataclass
import sys


def main():
    discs: list[Disc] = []
    for line in sys.stdin:
        words = line.strip().split(" ")
        positions = int(words[3])
        current_position = int(words[-1][:-1])
        discs.append(Disc(positions=positions, current_position=current_position))

    time = 0
    while not is_aligned(discs, time):
        time += 1

    print(f"Part 1: {time}")

    discs.append(Disc(positions=11, current_position=0))
    time = 0

    while not is_aligned(discs, time):
        time += 1

    print(f"Part 2: {time}")


@dataclass
class Disc:
    positions: int
    current_position: int

    def tick(self):
        self.current_position = (self.current_position + 1) % self.positions


def is_aligned(discs: list[Disc], time: int) -> bool:
    for i, disc in enumerate(discs):
        if (disc.current_position + i + 1 + time) % disc.positions != 0:
            return False

    return True


if __name__ == "__main__":
    main()
