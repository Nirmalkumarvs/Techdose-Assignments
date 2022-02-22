class Solution(object):
    def isValid(self, s):
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for p in s:
            if p in dic:
                stack.append(dic[p])
            elif p not in dic:
                if len(stack) == 0 or stack.pop() != p:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        
