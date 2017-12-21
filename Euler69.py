from Euler import prime_sieve
def Euler69():
    maxx = 1
    for p in prime_sieve(20):
        if maxx*p>1000000: return (maxx)
        maxx *=p
    return "more"

print Euler69()