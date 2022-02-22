#radix sort

a=[10,100,946,246,87,3777,764,494,663,536]
n=len(a)
b=[0]*n
maxi=max(a)
k=0
tp=1 
while tp<=maxi:
    count=[0]*10
    for j in range(n):
        count[a[j]//(tp)%10]+=1
        
    for j in range(1,10):
        count[j]+=count[j-1]
    
    for j in range(n-1,-1,-1):
        key=a[j]//tp%10
        b[count[key]-1]=a[j]
        count[key]-=1
        
    a=b[::]
    tp=tp*10
    
    print(a)
print(*a)



