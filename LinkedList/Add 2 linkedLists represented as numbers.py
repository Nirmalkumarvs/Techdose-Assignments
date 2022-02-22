head=head1=head2=None
tail=tail1=tail2=None

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


a=[1,2,3,4,5,6]

for i in a:
    if head1==None:
        head1=node(i)
        tail1=head1
    else:
        tail1.next=node(i)
        tail1=tail1.next
traverse(head1)

b=[1,2,3,4,5,6]

for i in b:
    if head2==None:
        head2=node(i)
        tail2=head2
    else:
        tail2.next=node(i)
        tail2=tail2.next
traverse(head2)        


head=node(0)
temp,temp1,temp2=head,head1,head2
carry=0

while(temp1 or temp2):
    x=temp1.val if temp1 else 0
    y=temp2.val if temp2 else 0
    x=x+y+carry
    carry=x//10
    temp.next=node(x%10)
    temp=temp.next
    temp1 = temp1.next if temp1 else None
    temp2 = temp2.next if temp2 else None
if carry:
    temp.next=node(carry)
    
traverse(head.next)
