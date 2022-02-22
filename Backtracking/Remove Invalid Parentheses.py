class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def is_valid(w):
            if not w:
                return True
            bal = 0
            for ch in w:
                if ch == '(':
                    bal += 1
                elif ch ==')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0
        
        def dfs(w):
            nonlocal res, seen, max_so_far
            
            if is_valid(w):
                res.add(w)
                max_so_far = max(max_so_far, len(w))
            else:
                for i,ch in enumerate(w):
                    if ch in '()':
                        word = w[:i] + w[i+1:]
                        if word in seen or len(word) < max_so_far:
                            continue
                        else:
                            seen.add(word)
                            dfs(word)
        
        res = set()
        seen = set()
        max_so_far = 0
        dfs(s)
        maxlen = max(map(len, res))
        return filter(lambda x: len(x) == maxlen, res)
