T = int(raw_input())
dictday={0:"monday",
1:"tuesday",
2:"wednesday",
3:"thursday",
4:"friday",
5:"saturday",
6:"sunday"
}
z = [2100,2200,2300]
def day(k):
    if k == 1900:
        return dictday[0]
    else:
        summ=-1
        for i in range(1900,k):
            if i % 4 == 0 and i not in z:
                summ+=2
            else:
                summ+=1
    return dictday[(summ % 7)]       
for i in range(T):
    print day(int(raw_input()))