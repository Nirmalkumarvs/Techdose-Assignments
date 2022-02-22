def isprime(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


n=int(input())

if isprime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    
