
head=None
tail=None

class node:
    def __init__(self,val):
        self.val=val
        self.next=None

a=[1,2,3,4,5,6]
k=3
for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        tail=tail.next
tail.next=head


 
ptr1 = head
ptr2 = head
while (ptr1.next != ptr1):
    count = 1
    while (count != k):
        ptr2 = ptr1
        ptr1 = ptr1.next
        count += 1

    ptr2.next = ptr1.next
    ptr1 = ptr2.next
 
print("Last person left standing (Josephus Position) is ", ptr1.val)


