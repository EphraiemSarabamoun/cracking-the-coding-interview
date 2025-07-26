def count_of_2s(n: int) -> int:
    count = 0
    length = len(str(n))
    for digit_place in range(length):
        power_of_10 = 10 ** digit_place
        next_power_of_10 = power_of_10 * 10
        right = n % power_of_10
        digit = (n // power_of_10) % 10
        left = n // next_power_of_10
        if digit > 2:
            count += (left + 1) * power_of_10
        elif digit == 2:
            count += left * power_of_10 + right + 1
        else:
            count += left * power_of_10
    return count