class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = Counter(s)     
        ans = [k*v for k, v in sorted(hashmap.items(), key=lambda x:x[1], reverse=True)]
        return (''.join(ans))
