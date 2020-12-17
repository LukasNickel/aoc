import copy


def part1(puzzle):
    visited = []
    position = 0
    acc = 0
    while True:
        if position in visited:
            return acc
        visited.append(position)
        op, arg = puzzle[position].split()
        arg = int(arg)
        if op == 'nop':
            position += 1
        elif op == 'acc':
            acc += arg
            position += 1
        elif op == 'jmp':
            position += arg
    return -1


def run_program(puzzle):
    visited = []
    position = 0
    acc = 0
    while True:
        if position == len(puzzle):
            return acc
        if position in visited:
            raise Exception('Loop')
        visited.append(position)
        op, arg = puzzle[position].split()
        arg = int(arg)
        if op == 'nop':
            position += 1
        elif op == 'acc':
            acc += arg
            position += 1
        elif op == 'jmp':
            position += arg
    return -1


def swap_instruction(op, arg):
    if op == 'jmp':
        return f'nop {arg}'
    elif op == 'nop':
        return f'jmp {arg}'


def part2(puzzle):
    # Ok, I'm too dumb for this, lets do it brute force
    for i, line in enumerate(puzzle):
        fixed = copy.deepcopy(puzzle)
        op, arg = line.split()
        arg = int(arg)
        if op == 'acc':
            continue
        else:
            fixed[i] = swap_instruction(op, arg)

        try:
            run_program(fixed)
            print('Works with fixing line', i, line)
            break
        except:
            continue

    # yes this is duplicate. sue me
    return run_program(fixed)


def main():
    with open('input') as f:
        puzzle = f.readlines()
    with open('example') as f:
        example = f.readlines()

    assert part1(example) == 5
    print('Solution Part 1:', part1(puzzle))

    assert part2(example) == 8
    print('Solution Part 2:', part2(puzzle))


if __name__ == '__main__':
    main()
