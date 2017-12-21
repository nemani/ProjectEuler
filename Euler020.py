def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
sum=0
k = str(factorial(100))
for i in k:
    sum+=int(i)
print sum