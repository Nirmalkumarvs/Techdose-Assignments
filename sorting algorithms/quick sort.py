#quick sort
def quicksort(a,start,end):
    if start<end: 
        pivot=partition(a,start,end)
        quicksort(a,start,pivot-1)
        quicksort(a,pivot+1,end)


def partition(a,left,right):
    l=left
    r=right
    pivot=a[left]
    while(l<r):
        while(l<r and a[l]<=pivot):
            l+=1
        while a[r]>pivot:
            r-=1
        if l<r:
            a[l],a[r]=a[r],a[l]
    a[r],a[left]=a[left],a[r]
    
    return r


a=[10,1,9,2,8,3,7,4,5]
n=len(a)


quicksort(a,0,n-1)
print(a)
        
