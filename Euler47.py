def factor(n):
    """
    find the prime factors of n along with their frequencies. Example:

    >>> factor(786456)
    [(2,3), (3,3), (11,1), (331,1)]
    """
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        n /= p
        while n%p == 0:
            n /= p
        F.append(p)
    F.sort()
    return F


def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

for i in range(200000):
    if len(factor(i))==4:
        if len(factor(i+1))==4 and len(factor(i+2))==4 and len(factor(i+3))==4:
            print i
            break