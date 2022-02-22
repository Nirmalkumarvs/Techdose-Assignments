class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class Stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        if self.top==None:
            self.top=Node(data)
            return
        new=Node(data)
        new.next=self.top
        self.top=new
        
    def printStack(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next
     
    def reverse(self):
        curr,prev,succ=self.top,self.top,self.top
        curr=curr.next
        prev.next=None
        while curr:
            succ=curr.next
            curr.next=prev
            prev=curr
            curr=succ
        self.top=prev
        
            
stack=Stack()
for i in  range(7):
    stack.push(i)
stack.reverse()
stack.printStack()
