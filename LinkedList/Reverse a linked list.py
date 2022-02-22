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

def rev(root):
    if root.next==None:
        head=root
        return
    rev(root.next)
    
    temp=root.next
    temp.next=root
    root.next=None

    
    
a=[1,2,3,4,5,6]

for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        tail=tail.next

traverse(head)

prev=head
curr=head.next
prev.next=None

while(curr):
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next


head,tail=tail,head 
traverse(head)

rev(head)
temp=head=tail
traverse(tail)

