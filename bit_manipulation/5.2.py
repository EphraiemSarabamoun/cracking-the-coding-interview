def binary_to_string(num: float) -> str:
    if num >= 1 or num < 0:
        return "ERROR"
    result = "0."
    bits = 0
    while num > 0 and bits < 32:
        num *= 2
        if num >= 1:
            result += '1'
            num -= 1
        else:
            result += '0'
        bits += 1
    return result if num == 0 else "ERROR"

if __name__ == "__main__":
    print(binary_to_string(0.72))
    