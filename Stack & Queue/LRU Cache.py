class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = dict()

    def get(self, key: int) -> int:
        if key not in self.__cache.keys():
            return -1
        else:
            value = self.__cache[key] 
            self.__cache.pop(key)
            self.__cache[key] = value 
           
            return value

    def put(self, key: int, value: int) -> None:
        if key in self.__cache.keys():  
            self.__cache.pop(key)
      
        
        self.__cache[key] = value
       
        if len(self.__cache.keys()) > self.__capacity: 
           
            keyToRemove = next(iter(self.__cache.keys())) 
           
            if keyToRemove != key:
                self.__cache.pop(keyToRemove) 
           
