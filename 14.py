import sys
from hashlib import md5

salt = sys.stdin.readline().strip()


def main():
    keys: list[tuple[int, str]] = []

    index = 0
    while len(keys) < 64:
        key = test_key(index)
        if key is not None:
            keys.append((index, key))

        index += 1

    print("Part 1:", index - 1)


def test_key(index: int) -> str | None:
    hash = get_hash(index)
    repeat = None
    for i in range(len(hash) - 2):
        if hash[i] == hash[i + 1] and hash[i] == hash[i + 2]:
            repeat = hash[i]
            break

    if repeat is None:
        return None

    for j in range(1000):
        new_index = index + j + 1
        new_hash = get_hash(new_index)
        s = "".join(repeat for _ in range(5))
        if s in new_hash:
            return hash

    return None


hash_cache: dict[int, str] = {}


def get_hash(index: int) -> str:
    try:
        return hash_cache[index]
    except KeyError:
        hash = md5(f"{salt}{index}".encode("utf-8")).hexdigest()
        hash_cache[index] = hash
        return hash


if __name__ == "__main__":
    main()
