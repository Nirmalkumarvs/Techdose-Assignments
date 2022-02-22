head=None
tail=None

class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def traverse(root):
    temp=root
    while(temp.next):
        print(temp.val,end="->")
        temp=temp.next
    print(temp.val)

def mergesort(root):
    if not root or not root.next:
        return root

    left=root
    right=mid(root)
    temp=right.next
    right.next=None
    right=temp
    
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right)

def merge(left,right):
    dhead=tail=node(1)
    while left and right:
        if left.val<right.val:
            tail.next=left
            left=left.next
        else:
            tail.next=right
            right=right.next
        tail=tail.next
        
    if left:
        tail.next=left
    if right:
        tail.right=right

    return dhead.next

def mid(root):
    slow=root
    fast=slow.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

        
a=[1,2,3,4,5,6]
a=a[::-1]

for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        tail=tail.next

print("Before sorting")
traverse(head)
head=mergesort(head)
print("\nAfter sorting")
traverse(head)
