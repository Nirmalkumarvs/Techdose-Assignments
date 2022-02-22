class MyStack(object):
    
    
    def __init__(self):
        self.nums=[]
    def push(self, x):
        self.nums.append(x)
       

    def pop(self):
        prev=-1
        while self.nums: 
            k=self.nums.pop(0)
            if k==-1: 
                break 
            self.nums.append(prev)
            prev=k
        return prev

    def top(self):
        k=self.pop() 
        self.nums.append(k) 
        return k
        

    def empty(self):
        return self.nums==[]
