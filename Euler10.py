from math import sqrt; from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))
output=[]
for i in range(2000000):
    if isPrime(i):
        output.append(i)
print output
print sum(output)