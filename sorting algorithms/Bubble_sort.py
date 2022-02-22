#Bubble sort
a=[10,9,8,7,6,5,4,3,2,1]
n=len(a)
for i in range(n-1):
    f=True
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            f=False
            a[j],a[j+1]=a[j+1],a[j]
    if f:
        break
print(*a)
            
