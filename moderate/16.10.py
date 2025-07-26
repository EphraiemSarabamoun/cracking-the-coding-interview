class Person:
    def __init__(self, birth: int, death: int):
        self.birth = birth
        self.death = death

def living_people(people: list[Person]) -> int:
    delta = [0] * 102  # 1900-2001
    for p in people:
        delta[p.birth - 1900] += 1
        delta[p.death - 1900 + 1] -= 1
    max_alive = alive = 0
    max_year = 1900
    for i in range(101):
        alive += delta[i]
        if alive > max_alive:
            max_alive = alive
            max_year = 1900 + i
    return max_year