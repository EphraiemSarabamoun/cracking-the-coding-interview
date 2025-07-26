class UF:
    def __init__(self, names: list[str]):
        self.parent = {name: name for name in names}
        self.rank = {name: 0 for name in names}

    def find(self, x: str) -> str:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def baby_names(freq: dict[str, int], synonyms: list[tuple[str, str]]) -> dict[str, int]:
    uf = UF(list(freq.keys()))
    for a, b in synonyms:
        uf.union(a, b)
    group_sum = {}
    for name in freq:
        root = uf.find(name)
        group_sum[root] = group_sum.get(root, 0) + freq[name]
    result = {}
    for name in freq:
        root = uf.find(name)
        result[name] = group_sum[root]
    return result