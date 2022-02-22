from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = {}
        for word in wordDict:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[0] = 0
                
        @lru_cache(None)
        def get_sentences(remaining):
            out = []
            if not remaining:
                return out
            node = trie
            current = ""
            for i, c in enumerate(remaining):
                if c not in node:
                    break
                node = node[c]
                current += c
                if 0 in node:
                    if i == len(remaining)-1:
                        out.append(current)
                    out += [current + " " + rest for rest in get_sentences(remaining[i+1:])]
            return out
        return get_sentences(s)
