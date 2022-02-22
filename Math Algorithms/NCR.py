from math import gcd
n,r = map(int,input().split())
p=1
d=1
if n-r<r:
    r=n-r
if r!=0:
    while r:
        p=p*n
        d=d*r
        gcdval=gcd(p,d)
        p=p//gcdval
        d=d//gcdval
        print(p,d)
        n-=1
        r-=1
print(p/d)
        
