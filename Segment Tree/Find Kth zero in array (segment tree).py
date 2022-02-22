
from math import gcd
st=[]

def build(st_idx,arr,start,end):
    if start>end:
        return
    if start==end:
        if arr[start]==0:
            st[st_idx]=1
        else:
            st[st_idx]=0
        return
    mid=(start+end)//2
    build(2*st_idx,arr,start,mid)
    build(2*st_idx+1,arr,mid+1,end)
    st[st_idx]=st[2*st_idx]+st[2*st_idx+1]



def find_kth(st_idx, start, end, k):
  
    if (st[st_idx] < k):
        return -1

    if (start == end):
        return start

    mid = (start + end) // 2;
    goLeft = st[st_idx * 2] >= k
    nextIndex = st_idx * 2 + (0 if goLeft else 1)
    nextLow = start if goLeft else mid + 1
    nextHigh = mid if goLeft else end
    nextK = k if goLeft else(k - st[st_idx * 2])

    return find_kth(nextIndex, nextLow, nextHigh, nextK)



arr=[4,8,0,0,0,4,0,6]
n=len(arr)
st=[0]*4*n
start,end=0,n-1
st_idx=1
build(st_idx,arr,start,end)

print(st)
for i in range(4):
    print(find_kth(st_idx,0,n-1,i+1))
print(st)


 
