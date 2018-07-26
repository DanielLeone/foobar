from math import floor, sqrt

# Store sqrt(2) as a very big int
SQRT2MINUS1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


def answer(n):
    return str(int(recurse(int(n))))


def answer_brute_force(n):
    return str(int(sum(floor(i * sqrt(2)) for i in xrange(1, int(n) + 1))))


def recurse(n):
    if n == 0:
        return 0
    else:
        n_prime = str(int(n) * SQRT2MINUS1)
        if len(n_prime) > len(str(SQRT2MINUS1)):
            n_prime = int(n_prime[:len(n_prime) - len(str(SQRT2MINUS1))])
        else:
            n_prime = 0
        return (n_prime + n) * (n_prime + n + 1) / 2 - n_prime * (n_prime + 1) - recurse(n_prime)
