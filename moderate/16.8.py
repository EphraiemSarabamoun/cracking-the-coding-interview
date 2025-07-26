def english_int(num: int) -> str:
    if num == 0:
        return "Zero"
    if num < 0:
        return "Negative " + english_int(-num)
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    groups = ["", "Thousand", "Million", "Billion"]
    result = []
    group_idx = 0
    while num > 0:
        part = num % 1000
        if part > 0:
            part_str = []
            if part // 100 > 0:
                part_str.append(ones[part // 100] + " Hundred")
            if part % 100 >= 20:
                part_str.append(tens[(part % 100) // 10])
                if part % 10 > 0:
                    part_str.append(ones[part % 10])
            elif part % 100 > 0:
                part_str.append(ones[part % 100])
            if group_idx > 0:
                part_str.append(groups[group_idx])
            result.append(" ".join(part_str))
        num //= 1000
        group_idx += 1
    return " ".join(reversed(result))