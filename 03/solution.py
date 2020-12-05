def move(right, down, position, puzzle):
    return (
        position[0] + down,
        (position[1] + right) % (len(puzzle[0])-1),
    )


def traverse(movement, puzzle):
    position = [0, 0]
    trees = 0
    while(position[0] < len(puzzle)):
        element = puzzle[position[0]][position[1]]
        if element == '#':
            trees += 1
        position = move(movement[0], movement[1], position, puzzle)
    return trees


def main():
    with open("input") as f:
        puzzle = f.readlines()
    print(
        'Solution Part 1:',
        traverse((3, 1), puzzle)
    )

    # Part two
    print('')
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    r = 1
    for s in slopes:
        trees = traverse(s, puzzle)
        print(trees)
        r *= trees
    print(r)


if __name__ == '__main__':
    main()
