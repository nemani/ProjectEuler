from Euler import is_prime
def trunc_l(k):
    sett =set([k])
    while len(str(k))>1:
        k = int((str(k)[1:]))
        sett.add(k)
    return sett
def trunc_r(k):
    sett =set([k])
    while len(str(k))>1:
        k = int((str(k)[:-1]))
        sett.add(k)
    return sett
def l_p(p):
    for i in trunc_l(p):
        if not is_prime(i):
            return False
    return True
def r_p(p):
    for i in trunc_r(p):
        if not is_prime(i):
            return False
    return True
k,a,ans=0,10,[]
while k < 11:
    if l_p(a):
        if r_p(a):
            k+=1
            ans.append(a)
    a+=1
print ans,k