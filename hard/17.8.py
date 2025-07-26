class Person:
    def __init__(self, height: int, weight: int):
        self.height = height
        self.weight = weight

def circus_tower(people: list[Person]) -> int:
    people.sort(key=lambda p: (p.height, p.weight))
    dp = [1] * len(people)
    max_tower = 1
    for i in range(1, len(people)):
        for j in range(i):
            if people[j].height < people[i].height and people[j].weight < people[i].weight:
                dp[i] = max(dp[i], dp[j] + 1)
        max_tower = max(max_tower, dp[i])
    return max_tower