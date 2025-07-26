def find_duplicates(sorted_file: str) -> list[int]:
    dups = []
    with open(sorted_file, 'r') as f:
        prev = f.readline().strip()
        for line in f:
            curr = line.strip()
            if curr == prev:
                if not dups or dups[-1] != int(curr):
                    dups.append(int(curr))
            prev = curr
    return dups