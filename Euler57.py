n = 3
d = 2
c = 0

for i in range(2,1000):
    n,d = n+d*2,n+d
    if len(str(n))>len(str(d)):c+=1

print "Solution to Euler 57 is:",c