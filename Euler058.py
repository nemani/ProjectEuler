from time import time
from Euler import miller_rabin as m_r

start = time()
n = 3
count = 3
q=set([1,3,5,7,9])

while (float(count)*100)/len(q) >= 10:
    n+=2
    count += m_r(n**2 - (n-1)) + m_r(n**2 - 2*(n-1)) + m_r(n**2 - 3*(n-1))
    q.update((n**2,n**2 - (n-1), n**2 - 2*(n-1), n**2 - 3*(n-1)))

print "Solution to Euler 58:",n,"found in",time() - start,"seconds"