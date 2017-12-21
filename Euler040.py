k=""
n=1
while len(k)<1000000:
    k += str(n)
    n += 1
print int(k[0])*int(k[9])*int(k[99])*int(k[999])*int(k[9999])*int(k[99999])*int(k[999999])