import numpy as np
from copy import deepcopy


def part1(puzzle):
    # assuming there is one such chain and we dont need to find another:
    puzzle = deepcopy(puzzle)
    puzzle += [0, max(puzzle)+3]
    puzzle.sort()
    puzzle = np.array(puzzle)
    diffs = puzzle[1:] - puzzle[:-1]
    v = np.count_nonzero((diffs == 1))
    vvv = np.count_nonzero((diffs == 3))
    return v * vvv


def part2(puzzle):
    """
    I couldnt figure this one out myself.
    Very helpful discussion here:
    https://www.reddit.com/r/adventofcode/comments/kabi91/2020_day_10_closedform_mathematical_solution/gfaq3zj/
    I basically copied the code from mrbengi96
    """
    puzzle = deepcopy(puzzle)
    puzzle += [0, max(puzzle)+3]
    puzzle.sort()

    # Special case for the first three entries to start
    a = 1 if 1 in puzzle else 0
    b = a + 1 if 2 in puzzle else 0
    c = a + b + 1 if 3 in puzzle else 0

    # This basically describes the ways to get to the
    # joltage at index i given the possible values from before
    # The rules define the max diff as 3, thats why theres three
    # values and with each iteration the last one is disregarded
    # as it cant contribute any longer
    for i in range(4, max(puzzle) + 1):
        a, b, c = b, c, a + b + c if i in puzzle else 0
    return c


def main():
    with open('input') as f:
        puzzle = [int(l) for l in f.readlines()]
    with open('example') as f:
        example = [int(l) for l in f.readlines()]
    with open('example2') as f:
        example2 = [int(l) for l in f.readlines()]

    assert part1(example) == 35
    assert part1(example2) == 220
    print('Solution Part 1:', part1(puzzle))

    assert part2(example) == 8
    assert part2(example2) == 19208
    print('Solution Part 2:', part2(puzzle))


if __name__ == '__main__':
    main()
