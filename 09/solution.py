from itertools import combinations


def part1(puzzle, plength=25, n=25):
    indices_to_test = range(plength, len(puzzle) - 1)
    for i in indices_to_test:
        if not valid(puzzle[i], puzzle[i-n:i]):
            return puzzle[i]
    return -1


def valid(number, previous):
    for c in combinations(previous, 2):
        if sum(c) == number:
            return True
    return False


def part2(puzzle, weak_number=-1):
    for i in range(0, len(puzzle)):
        sum_seq = 0
        for j in range(i, len(puzzle)):
            sum_seq += puzzle[j]
            if sum_seq == weak_number:
                seq = puzzle[i:j+1]
                return min(seq) + max(seq)
            elif sum_seq > weak_number:
                break
    return -1


def main():
    with open('input') as f:
        puzzle = [int(l) for l in f.readlines()]
    with open('example') as f:
        example = [int(l) for l in f.readlines()]

    assert part1(example, plength=5, n=5) == 127
    print('Solution Part 1:', part1(puzzle))

    assert part2(example, 127) == 62
    print('Solution Part 2:', part2(puzzle, part1(puzzle)))


if __name__ == '__main__':
    main()
