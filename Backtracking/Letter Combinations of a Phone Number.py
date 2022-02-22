class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def make_letter(idx: int, letter: str) -> None : 
            
            if idx == len(digits) :
                ans.append(letter)
                return
            
         
            for i in phone_keyboard[digits[idx]] : 
                make_letter(idx + 1, letter + i)
        
        ans = []
        
        if not digits : 
            return ans
        
        phone_keyboard = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'],
                          '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
                          '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                          '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        
        make_letter(0, "")
        
        print(ans)
        return ans
