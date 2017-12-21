def pow5(k):
    summ=0
    for i in range(len(str(k))):
        summ+=int(str(k)[i])**5
    return summ
    
ans = 0
for i in range(2,1000000):
    if i == pow5(i):
        ans+=i
print ans