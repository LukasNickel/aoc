import re


def has_fields(passport):
    valid = (
        ('byr:' in passport)
        & ('iyr:' in passport)
        & ('eyr:' in passport)
        & ('hgt:' in passport)
        & ('hcl:' in passport)
        & ('ecl:' in passport)
        & ('pid:' in passport)
    )
    cid = ('cid:' in passport)
    return valid, cid


def check_number(value, min_valid, max_valid, l_valid):
    if not len(value) == l_valid:
        return False
    if not value.isdigit():
        return False
    if not (
        (int(value) >= min_valid)
        & (int(value) <= max_valid)
    ):
        return False
    return True


def valid_values(passport):
    for field in passport.split():
        key, value = field.split(':')
        if key == 'byr':
            if not check_number(value, 1920, 2002, 4):
                return False
        elif key == 'iyr':
            if not check_number(value, 2010, 2020, 4):
                return False
        elif key == 'eyr':
            if not check_number(value, 2020, 2030, 4):
                return False
        elif key == 'hgt':
            if len(value) < 4:  # 2 unit, at least 2 value
                return False
            unit = value[-2:]
            numeric_value = value[:-2]
            if unit == 'cm':
                if not check_number(numeric_value, 150, 193, 3):
                    return False
            elif unit == 'in':
                if not check_number(numeric_value, 59, 76, 2):
                    return False
        elif key == 'hcl':
            if not re.compile(r'^#[a-f0-9]{6}$').match(value):
                return False
        elif key == 'ecl':
            valids = (
                'amb',
                'blu',
                'brn',
                'gry',
                'grn',
                'hzl',
                'oth',
            )
            if value not in valids:
                return False
        elif key == 'pid':
            if not re.compile(r'^[0-9]{9}$').match(value):
                return False

    return True


def check_batch(batch):
    n_valid = 0
    for passport in batch.split('\n\n'):
        if has_fields(passport)[0]:
            if valid_values(passport):
                n_valid += 1
    return n_valid


def main():
    with open('input') as f:
        batch = f.read()
    passports = batch.split('\n\n')
    valid_passports = 0
    for passport in passports:
        valid, cid = has_fields(passport)
        if valid:
            valid_passports += 1
    print('Solution part 1:', valid_passports)

    # Part Two
    print('')
    with open('valids') as f, open('invalids') as g:
        valids = f.read()
        invalids = g.read()

    print('Valid test:', check_batch(valids))
    print('Invalid test:', check_batch(invalids))
    print('Solution part 2:', check_batch(batch))
    return 0


if __name__ == '__main__':
    main()
