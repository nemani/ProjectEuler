def is_pd9(t):
    t = str(t)
    if "0" not in t and len(t)==9:
        if "1" in t and "2" in t and "3" in t and "4" in t and "5" in t and "6" in t and "7" in t and "8" in t and "9" in t:
            return True
d = 0
for a in range(1,10000):
    n=1
    k=""
    while len(k)<9:
        k+=str(a * n)
        n+=1
    if int(k)>d and is_pd9(k):
        d= int(k)
        print k
print d