output=[1,2]
for i in range(1000):
    c = output[i]+ output[i+1]
    output.append(c)
    if c>4000000:
        print 'STOP'
        break
sum = 0
for i in output:
    if i%2==0:
        sum+=i
print sum