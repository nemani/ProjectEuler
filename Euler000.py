listt=[]
for i in range(int(raw_input())):
    listt.append(raw_input().split())
max_lead =0
for a in listt:
    y = int(a[0])
    z = int(a[1])
    lead = abs(y - z)
    if lead > max_lead:
        max_lead = lead
        if y > z:
            winner =1
        elif z > y:
            winner =2

print str(winner)+ " " + str(max_lead)