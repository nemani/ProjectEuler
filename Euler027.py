from math import sqrt
def prime_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True
def numprimes(p,q):
    n=0
    while is_prime((n*n)+(p*n)+q):
        n+=1
    return n
d=0
for b in prime_sieve(1000):
    for a in range(-b,b,2):
        n=1
        while is_prime((n*n)+(a*n)+b):n+=1
        if n>d: d,p=n,a*b
print p,d