class Solution:
    def calcEquation(self, equations, values, queries):
        nums = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            nums[a][b] = v
            nums[b][a] = 1/v
        
        def find(a, b, seen=tuple()):
            if a in seen:
                return -1
            if a in nums:
                if b in nums[a]:
                    return nums[a][b]
                for x in nums[a]:
                    ans = nums[a][x] * find(x, b, seen +(a,))
                    if ans >= 0:
                        return ans
            return -1
            
        return [find(a,b) for a,b in queries]
