#selection sort

a=[5,7,3,8,2,9,10,18]
n=len(a)

for i in range(n-1):
    mini=i
    for j in range(i+1,n):
        if a[mini]>a[j]:
            mini=j
    a[mini],a[i]=a[i],a[mini] 
print(*a)
        
