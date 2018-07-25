from math import floor, sqrt


def answer(n):
    return answer_brute(n)


def answer_brute(n):
    n = int(n)
    c = 0
    x = 1
    while x <= n:
        c += floor(x * sqrt(2))
        x += 1
    return str(int(c))
