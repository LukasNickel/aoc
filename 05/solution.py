def bin_part(sequence, lower='F', upper='B', seats=list(range(128))):
    for sep in sequence:
        mid = len(seats)//2
        if sep == lower:
            seats = seats[0: mid]
        elif sep == upper:
            seats = seats[mid:]
    assert len(seats) == 1
    return seats[0]


def seat_id(sequence):
    row = bin_part(sequence[0:7])
    col = bin_part(
        sequence[-4:],
        lower='L',
        upper='R',
        seats=list(range(8)),
    )
    return row * 8 + col


def main():
    with open('input') as f:
        seats = f.readlines()

    assert seat_id('FBFBBFFRLR') == 357
    assert seat_id('BFFFBBFRRR') == 567
    assert seat_id('FFFBBBFRRR') == 119
    assert seat_id('BBFFBBFRLL') == 820

    ids = []
    for seat in seats:
        ids.append(seat_id(seat))
    print('Solution Part 1:', max(ids))

    possible_ids = list(range(0, 127*8+8+1))
    for id_ in possible_ids:
        if (id_ not in ids) and (id_ - 1 in ids) and (id_ + 1 in ids):
            print('Solution Part 2:', id_)


if __name__ == '__main__':
    main()
