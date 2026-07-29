class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxLen = 0
        subset = set()

        while j < len(s):
            while s[j] in subset:
                subset.remove(s[i])
                i += 1

            subset.add(s[j])
            maxLen = max(j-i+1, maxLen)
            j += 1

        return maxLen


        