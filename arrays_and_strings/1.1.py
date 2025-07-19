def is_unique(string: str) -> bool:
    my_set = set()
    for char in string:
        if char in my_set:
            return False
        my_set.add(char)
    return True


if __name__ == "__main__":
    print(is_unique("hello"))
    print(is_unique("world"))
    print(is_unique("python"))
    print(is_unique("programming"))
