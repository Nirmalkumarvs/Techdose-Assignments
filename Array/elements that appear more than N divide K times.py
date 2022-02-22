
arr=[1,2,2,2,5,2,1,3,5]
b=[]
k=2
l=len(arr)
times=l//k
max=-1
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in dic:
    if dic[i]>=times:
        b.append(i)
print(*b)
        
        
    
    
    
