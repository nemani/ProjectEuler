import time 
a=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8] # 0 to 19
b={20:6, 30:6, 40:5, 50:5,60:5,70:7,80:6,90:6}
c=[11,12,13,14,15,16,17,18,19]
h=7
t=11
def fn(k):
    letters=0
    if k/100 != 0:
        letters+= a[k/100] + h #p hundred
        if k%100!=0: letters+=3 #and
        if k%100 == 10: letters+=3
    p=k%100-k%10
    if p in b:
        letters+=b[p]
    if k%100 in c:
        letters+=a[k%100]
    else:
        letters+=a[k%10]
    if k == 10:
        letters = 3
    return letters    
start=time.time()
ans=11
for i in xrange(1000):
    ans+=fn(i)
elapsed = (time.time() - start)
print 'Solution to Euler 17 is:%s found in %s seconds' % (ans,elapsed)