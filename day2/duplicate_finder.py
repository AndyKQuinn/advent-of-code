def find_duplicate_subsequences(number):
    """
    Check if the entire number is made up of a repeating pattern.

    For example:
    - 1122 = "11" repeated 2 times (pattern length 2)
    - 123123 = "123" repeated 2 times (pattern length 3)
    - 1111 = "1" repeated 4 times (pattern length 1)
    - 101010 = "10" repeated 3 times (pattern length 2)

    Args:
        number: Can be an int or string of digits

    Returns:
        List of tuples (pattern, repetitions) for valid repeating patterns found
    """

    digits = str(number)
    length = len(digits)
    patterns = []

    if length <= 1:
        return patterns

    for pattern_len in range(1, length // 2 + 1):
        # The length must be divisible by the pattern length
        if length % pattern_len != 0:
            continue

        # Extract first chunk as the pattern
        pattern = digits[:pattern_len]

        is_valid = True
        repetitions = length // pattern_len

        for i in range(repetitions):
            chunk = digits[i * pattern_len : (i + 1) * pattern_len]
            if chunk != pattern:
                is_valid = False
                break

        if is_valid and repetitions >= 2:
            patterns.append((pattern, repetitions))

    return patterns


def has_half_match(number):
    """Check if the first half of the number equals the second half."""
    digits = str(number)
    length = len(digits)

    if length % 2 != 0:
        return False  # Can't split evenly

    mid = length // 2
    first_half = digits[:mid]
    second_half = digits[mid:]

    return first_half == second_half
