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

def ispalindrome(right):
    global tail
    tail=head

    if right==None:
        return True

    flag = ispalindrome(right.next)
    if not flag:
        return False

    if tail.val==right.val:
        tail=tail.next
        return True
    else:
        return False
    
a=[6,5,4,3,1,3,4,5,6]

for i in a:
    if head==None:
        head=node(i)
        tail=head
    else:
        tail.next=node(i)
        tail=tail.next

traverse(head)

print(ispalindrome(head))
head=head.next
traverse(head)
print(ispalindrome(head))
