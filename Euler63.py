from math import log10
s = 0
for i in range(1,10):
    s+=int(1/(1-log10(i)))
print s