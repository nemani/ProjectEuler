output=[]
for i in range(100,1000):
    for k in range(100,1000):
        c = (i*k)
        a = str(c)
        b = a[::-1]
        if a==b:
         output.append(c)
print output
print max(output)