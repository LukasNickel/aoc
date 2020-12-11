from collections import defaultdict


def part1(puzzle, target='shiny gold bag'):
    contains = containment_rules(puzzle)
    result = set()
    check = [target]
    finished_searching = set()
    while True:
        try:
            target = check.pop()
        except IndexError:
            break
        if target in finished_searching:
            continue
        containing = find_containing(contains, target)
        check += containing
        finished_searching.update([target])
        result.update(containing)
    return len(result)


def part2(puzzle):
    rules = containment_with_numbers(puzzle)
    r = count_inner(rules, [1, "shiny gold bag"])
    return r-1  # 1 for the start bag


def find_containing(rules, target):
    result = []
    for outer, inner in rules.items():
        if target in inner:
            # Whitespace messes search up
            result.append(outer.strip())
    return result


def containment_rules(puzzle):
    contains = {}
    for line in puzzle:
        bag, content = line.split('contain')
        contains[bag.replace('bags', 'bag')] = content.replace('bags', 'bag')
    return contains


def containment_with_numbers(puzzle):
    contains = defaultdict(list)
    for line in puzzle:
        bag, content = line.replace('no', '0').replace('.', '').split(
            'contain'
        )
        for inner in content.split(','):
            contains[bag.replace('bags', 'bag').strip()].append(
                inner.replace('bags', 'bag').strip().split(" ", 1)
            )
    return contains


def count_inner(rules, target):
    if target[0] == '0':
        return 0
    n, bag = target
    n = int(n)
    new_bags = rules[bag]
    n_total = n
    for inner_target in new_bags:
        n_inside = count_inner(rules, inner_target)
        n_total += n*int(n_inside)
    return n_total


def main():
    with open('example') as f:
        example = f.readlines()
    with open('example2') as f:
        example2 = f.readlines()
    with open('input') as f:
        puzzle = f.readlines()

    assert part1(example) == 4
    print('Solution Part 1:', part1(puzzle))

    assert part2(example) == 32
    assert part2(example2) == 126
    print('Solution Part 2:', part2(puzzle))


if __name__ == '__main__':
    main()
