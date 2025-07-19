def urlify(string: str, length: int) -> str:
    string = string[:length]
    for char in string:
        if char == " ":
            string = string.replace(char, "%20")
    return string


if __name__ == "__main__":
    print(urlify("hello world", 11))
    print(urlify("hello world python", 18))
    print(urlify("hello world python  ", 19))

