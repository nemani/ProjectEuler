from Euler import prime_sieve
def pandigital(k):
    t=[1,2,3,4,5,6,7,8,9]
    z=[]
    k = str(k)
    for i in k:
        if int(i) not in t[:len(k)] or i in z:
                return False
        z.append(i)
    return True
d = 2143
for ii in prime_sieve(10000000):
    if pandigital(ii) and ii>d:
        d = ii
print d