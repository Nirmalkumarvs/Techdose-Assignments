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

def multiply(first_ptr, second_ptr):
  
    num1 = 0
    num2 = 0
    p=1
    while first_ptr != None or second_ptr != None:
        if first_ptr != None:
            num1 = (num1 ) + first_ptr.val*p
            first_ptr = first_ptr.next
    
        if second_ptr != None:
            num2 = (num2 ) + second_ptr.val*p
            second_ptr = second_ptr.next
        p=p*10
    num1 = num1 * num2
    
    dhead=node(0)
    temp=dhead
    while num1:
        temp.next=node(num1%10)
        temp=temp.next
        num1=num1//10
    return dhead.next 
    

a=[1,2,3,4,5]

for i in a:
    if head1==None:
        head1=node(i)
        tail1=head1
    else:
        tail1.next=node(i)
        tail1=tail1.next
traverse(head1)

b=[1,2,3,4,5]

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

head=multiply(head1,head2)
traverse(head)




