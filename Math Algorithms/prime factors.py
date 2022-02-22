n=int(input())
m=n
l=[]
for i in range(2,int(n**0.5)+1):
    while m>i and m%i==0:
        m=m//i
        l.append(i)
        if m==1:
            break
    if m==1:
        break
if m>1:
    l.append(m)
print(l)
