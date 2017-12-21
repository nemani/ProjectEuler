from Euler import prime_sieve

maxx = 1000000
k = prime_sieve(maxx)
prime_sum = [0]

summ = 0
count = 0
while (summ<maxx):
    summ += k[count]
    prime_sum.append(summ)
    count += 1

t = 0
for i in range(count):
    for a in range(t,count):
        n = sum(k[i:a+i]) 
        if n in k:
            if a > t:
                t = a        
                z = n
print z ,t