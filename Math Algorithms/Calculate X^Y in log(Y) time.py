a,b=map(int,input().split())
res=1

while b>0:
    if b&1:
        res = res * a
    a=a*a
    b=b//2
    

print(res)
    
