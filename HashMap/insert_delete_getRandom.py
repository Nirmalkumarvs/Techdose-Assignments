import random
class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = set()

    def insert(self, val: int) -> bool:
        if val in self.RandomizedSet:
            return False
        else:
            self.RandomizedSet.add(val)
            return True
            

    def remove(self, val: int) -> bool:
        if val in self.RandomizedSet:
            self.RandomizedSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        set_list = list(self.RandomizedSet)
        index = random.randint(0,len(set_list)-1)
        return set_list[index]
