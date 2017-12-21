from math import sqrt; from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))
a=13
k=0
output=[]
while k<10002:
    if isPrime(a):
        print a
        output.append(a)
        k+=1
    a+=2
print output[-1]