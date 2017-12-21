summ=[]
for i in range(100,1000):
    for j in range(10,100):
        k = i * j
        if len(str(k))==4:
            t = str(k)+str(i)+str(j)
            if "0" not in t:
                if "1" in t and "2" in t and "3" in t and "4" in t and "5" in t and "6" in t and "7" in t and "8" in t and "9" in t:
                    if k not in summ:
                        summ.append(k)
for i in range(1000,10000):
    for j in range(1,10):
        k = i * j
        if len(str(k))==4:
            t = str(k)+str(i)+str(j)
            if "0" not in t:
                if "1" in t and "2" in t and "3" in t and "4" in t and "5" in t and "6" in t and "7" in t and "8" in t and "9" in t:
                    if k not in summ:
                        summ.append(k)
print sum(summ)