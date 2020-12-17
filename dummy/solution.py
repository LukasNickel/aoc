def part1(puzzle):
    return -1


def part2(puzzle):
    return -1


def main():
    with open('input') as f:
        puzzle = f.readlines()
    with open('example') as f:
        example = f.readlines()

    assert part1(example) == 0
    print('Solution Part 1:', part2(puzzle))

    assert part2(example) == 0
    print('Solution Part 2:', part2(puzzle))


if __name__ == '__main__':
    main()
