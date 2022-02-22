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
    
def rev(root,k):
   
    curr=root
    prev=None
    next=None
    i=0
    while curr and i<k:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        i+=1

    if next:
        root.next=rev(next,k)

    return prev
        
        
a=[1,2,3,4,5,6,7,8,9,10,11]

for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        tail=tail.next
        
head=rev(head,3)
traverse(head)
