def is_palin(k): return(str(k) == str(k)[::-1])
ans=0
for i in range(1000000):
    if is_palin(i) and is_palin(bin(i)[2:]):
        ans+=i
print ans