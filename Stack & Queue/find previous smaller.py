arr=[1,0,7,6,7,8,5,3,2,6]
stack=[]
l=len(arr)
right=[0]*l
for i in range(l):
    k=arr[i]
    while stack and arr[stack[-1]]>=k:
        stack.pop(-1)
    if stack:
        right[i]=stack[-1]
    else:
        right[i]=None
    stack.append(i)
for i in right:
    if i==None:
        print(None,end=" ")
        continue
    print(arr[i],end=" ")
        
