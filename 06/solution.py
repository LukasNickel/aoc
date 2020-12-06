def part1(puzzle):
    groups = puzzle.split('\n\n')
    yes_answers = 0
    for group_answer in groups:
        counts = count_unique_yes(group_answer)
        yes_answers += counts
    return yes_answers


def part2(puzzle):
    groups = puzzle.split('\n\n')
    yes_answers = 0
    for group_answer in groups:
        counts = count_all_yes(group_answer)
        yes_answers += counts
    return yes_answers


def count_unique_yes(group_answer):
    sums = ""
    for person_answer in group_answer.split('\n'):
        sums += person_answer
    return len(set(sums))


def count_all_yes(group_answer):
    person_answers = group_answer.split('\n')
    candidates = set(person_answers[0])
    for person_answer in person_answers:
        # hack to avoid the eof leading to an "empty" answer for the last group
        if person_answer == '':
            continue
        candidates = candidates.intersection(set(person_answer))
    return len(candidates)


def main():
    with open('example') as f:
        example = f.read()
    with open('input') as f:
        puzzle = f.read()

    assert part1(example) == 11
    print('Solution Part 1:', part1(puzzle))

    assert part2(example) == 6
    print('Solution Part 2:', part2(puzzle))


if __name__ == '__main__':
    main()
