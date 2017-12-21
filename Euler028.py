def nex(n):
    return 7 - 10*n + 4*n**2
k=2
summ=1
for i in range(2,502):
    summ+=nex(i)*4+k*6
    k+=2
print summ