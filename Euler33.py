listt=[]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            a = float(str(i)+str(j))
            d = float(str(j)+str(k))
            if a/d == float(i)/float(k) and d>a:
                listt.append(a/d)
ans = 1
for i in listt:
    ans = ans*i
ans = 1/ans
print "solution to euler 33 is :", ans