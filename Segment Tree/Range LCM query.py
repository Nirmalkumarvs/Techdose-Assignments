from math import gcd


def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

st=[]

def build(st_idx,arr,start,end):
    if start>end:
        return
    if start==end:
        st[st_idx]=arr[start]
        return
    mid=(start+end)//2
    build(2*st_idx,arr,start,mid)
    build(2*st_idx+1,arr,mid+1,end)
    st[st_idx]=lcm(st[2*st_idx],st[2*st_idx+1])

def query(arr,srt,ed,start,end,st_idx):
    if start>ed or end<srt:
        return 1
    if start>=srt and end<=ed:
        return st[st_idx]
    
    mid=(start+end)//2
    left=query(arr,srt,ed,start,mid,2*st_idx)
    right=query(arr,srt,ed,mid+1,end,2*st_idx+1)
    return lcm(left,right)



def update(st_idx,arr,start,end,pos,newval):
    if start>pos or end<pos:
        return 
    if pos==end and start==pos:
        st[st_idx]=newval
        return

    mid=(start+end)//2
    update(2*st_idx,arr,start,mid,pos,newval)
    update(2*st_idx+1,arr,mid+1,end,pos,newval)
    st[st_idx]=st[2*st_idx]+st[2*st_idx+1]
    
        
arr=[4,8,4,2,6]
n=len(arr)
st=[0]*4*n
start,end=0,n-1
st_idx=1
build(st_idx,arr,start,end)

print(st)
for i in range(n):
    for j in range(i+1,n):
        print(query(arr,i,j,0,n-1,1))
        res=arr[i]
        for k in range(i+1,j+1):
            res=lcm(res,arr[k])
        print(res)
update(1,arr,0,n-1,5,7)
print(st)
