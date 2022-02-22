

#counting sort
a=[1,9,2,8,4,5,2,3,6,8,6,4,3,2,5,7,3,7,4,6,5]
n=len(a)
k=max(a)+1
count=[0]*k
b=[0]*(n)

for i in a:
    count[i]+=1
    
for i in range(1,k):
    count[i]+=count[i-1]

print(count)
for i in range(n-1,-1,-1):
    hsh=count[a[i]]
    
    b[hsh-1]=a[i]
    count[a[i]]-=1

print(*b)
    
