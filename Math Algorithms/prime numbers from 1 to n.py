#Find all prime number from 1 to N
n=int(input())
prime=[True]*(n+1)
prime[0],prime[1]=False,False
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(i+i,n+1,i):
            prime[j]=False

print(*[i for i in range(n+1) if prime[i]])
