def unique_in_order(iterable):
    new = []
    letter_before = None
    for value in iterable:
        if value == letter_before:
            continue
        letter_before = value
        new.append(value)
    return new



unique_in_order('AAAABBBCCDAABBB')
# Should be ['A', 'B', 'C', 'D', 'A', 'B']
