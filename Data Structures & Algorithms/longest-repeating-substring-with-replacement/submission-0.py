class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLen = 0
        i = 0
        j = 0

        while j < len(s):
            count[s[j]] = 1 + count.get(s[j], 0)

            while (j-i+1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j-i+1)
            j += 1

        return maxLen

        