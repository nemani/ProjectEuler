def next_num(k):
    return k + int(str(k)[::-1])
def is_palin(k):
    return(str(k)==str(k)[::-1])

        
ans=[]
for i in range(1,10000):
    itter=0
    a = i
    while itter<50:
        a,itter = next_num(a), itter +1
        if is_palin(a):
            break
    if itter ==50:
        ans.append(i)
print 'Solution to Euler 55:' , len(ans)