class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        
        pCounter = [0] * 26
        for char in p:
            pCounter[ord(char) - ord('a')] += 1
        
    
        sCounter = [0] * 26
        for char in s[:len(p)-1]:
            sCounter[ord(char) - ord('a')] += 1
        
        for i in range(len(p) - 1, len(s)):
            sCounter[ord(s[i]) - ord('a')] += 1
            if sCounter == pCounter:
                ans.append(i-len(p)+1)
            sCounter[ord(s[i-len(p)+1]) - ord('a')] -= 1            

        return ans
