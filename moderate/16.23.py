import random

def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        num = (rand5() - 1) * 5 + rand5()
        if num <= 21:
            return (num - 1) % 7 + 1