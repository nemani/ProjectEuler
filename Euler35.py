import time
def prime_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
def rotations_prime(k):
    k = str(k)
    listt=[k]
    for i in range(len(k)):
        k=k[1:]+k[0]
        if k not in listt: 
            listt.append(k)
    for i in listt:
        if int(i) not in list_prime:
            return False
    for i in listt:
        master_list.add(int(i))
    return True
start = time.time()
list_prime = set(prime_sieve(1000000))
master_list=set()
for i in list_prime:
    if i not in master_list:
        rotations_prime(i)
print len(master_list), time.time() - start