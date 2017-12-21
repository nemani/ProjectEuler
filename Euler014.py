def next_num(num):
    if num%2==0:
        return num/2
    else:
        return 3*num+1  
def chain_len(num):
    k=1
    while num !=1:
        num = next_num(num)
        k+=1
    return k
dict={}
output=[]
for i in range(100000,1000000):
    dict[chain_len(i)] = i
    output.append(chain_len(i))
print max(output)
print dict[max(output)]