def string_compression(string: str) -> str:
    if len(string) == 0:
        return string
    if len(string) == 1:
        return string + "1"
    count = 1
    compressed = ""
    previous_char = string[0]
    for char in string[1:]:
        if char == previous_char:
            count += 1
        else: 
            compressed += previous_char + str(count)
            previous_char = char
            count = 1
    compressed += char + str(count)
    return compressed


if __name__ == "__main__":
    print(string_compression("hello"))
    print(string_compression("world"))
    print(string_compression("python"))
    print(string_compression("programming"))
