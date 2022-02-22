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


a=[1,2,3,4,2,3,4,5,6,5,6]

for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        tail=tail.next

traverse(head)

dic={}
temp=head.next
curr=head
while(temp):
    if temp.val not in dic:
        dic[temp.val]=1
        temp=temp.next
        curr=curr.next
        
    temp=temp.next
curr.next=None


traverse(head)
