def pattern_matching(pattern: str, value: str) -> bool:
    if not pattern:
        return not value
    main_char = pattern[0]
    alt_char = 'b' if main_char == 'a' else 'a'
    count_main = pattern.count(main_char)
    count_alt = len(pattern) - count_main
    if count_alt == 0:
        return value.count(value[:len(value)//count_main]) == count_main if count_main > 0 else True
    for len_main in range(len(value) // count_main + 1):
        remaining = len(value) - len_main * count_main
        if count_alt == 0:
            if remaining == 0:
                str_main = value[:len_main]
                if all(value[i*len_main:(i+1)*len_main] == str_main for i in range(count_main)):
                    return True
        elif remaining % count_alt == 0:
            len_alt = remaining // count_alt
            pos = pattern.find(alt_char)
            str_main = value[0:len_main]
            str_alt = value[pos*len_main : pos*len_main + len_alt]
            if str_main == str_alt:
                continue
            constructed = ''
            for c in pattern:
                if c == main_char:
                    constructed += str_main
                else:
                    constructed += str_alt
            if constructed == value:
                return True
    return False