class MyHashMap(object):

    def __init__(self):
        self.dic={}

    def put(self, key, value):
        self.dic[key]=value
        
    
    def get(self, key):
        if key in self.dic:
            return self.dic[key] 
        return -1
        

    def remove(self, key):
        if key in self.dic: 
            del self.dic[key] 
        else:
            return -1
