class Solution(object):
    def lengthOfLongestSubstring(self, s):
     
        var = {}
        maxlen = l = 0
        for r, c in enumerate(s):
            if c in var and l <= var[c]:
                maxlen = max(maxlen, r - l)
                l = var[c] + 1
            var[c] = r
        maxlen = max(maxlen, len(s) - l)
        return maxlen
