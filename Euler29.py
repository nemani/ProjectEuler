listt=[]
for a in range(2,101):
    for b in range(2,101):
        if not(a**b in listt):
            listt.append(a**b)
print len(listt)