class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        results = []
        
        def backtracking(startIndex, path):
            if startIndex == len(s):
                results.append(' '.join(path))
            else:
                for word in wordDict:
                    if startIndex + len(word) > len(s):
                        continue
                    else:
                        if s[startIndex : startIndex + len(word)] == word:
                            backtracking(startIndex + len(word), path + [word])
        backtracking(0, [])
        return results
