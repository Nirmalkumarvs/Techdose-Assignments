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

def isloop(root):
    slow=root
    fast=root
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast and slow:
            return True
    return False

a=[1,2,3,4,5,6]

for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        if i==4:
            four=tail.next
        if i==5:
            five=tail.next
        tail=tail.next
        
tail.next=None
print(isloop(head))

tail.next=five
print(isloop(head))
