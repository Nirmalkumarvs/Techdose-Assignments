
def mergesort(a,left,right):
    if left<right:
        mid=(left+right)//2
        mergesort(a,left,mid)
        mergesort(a,mid+1,right)
        merge(a,left,mid,right)

def merge(a,left,mid,right):
    i=left
    j=mid+1
    k=left
    while i<=mid and j<=right:
        if a[i]<a[j]:
            b[k]=a[i]
            i+=1
        else:
            b[k]=a[j]
            j+=1
        k+=1
    while i<=mid:
        b[k]=a[i]
        i,k=i+1,k+1
    while j<=right:
        b[k]=a[j]
        j,k=j+1,k+1
    for i in range(left,right+1):
        a[i]=b[i]
    print(a[left:right+1])
        


#merge sort
a=[10,1,9,2,8,3,7,4,6,5]
n=len(a)
b=[0]*(n+1)
mergesort(a,0,n-1)
print(*a)

