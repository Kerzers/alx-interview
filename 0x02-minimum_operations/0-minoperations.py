#!/usr/bin/python3
'''Minimum Operations challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chars = 1
    clipboard = 0
    count = 0

    while pasted_chars < n:
        if clipboard == 0:
            clipboard = pasted_chars
            count += 1

        # if haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            count += 1
            continue

        remaining = n - pasted_chars
        if remaining < clipboard:
            return 0

        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            count += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increment operations counter
            count += 2

    if pasted_chars == n:
        return count
    else:
        return 0
