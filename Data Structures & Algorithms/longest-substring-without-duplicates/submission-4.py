class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        output = 0

        i = 0
        j = 0

        while j < len(s):
            while s[j] in unique:
                unique.remove(s[i])
                i += 1

            unique.add(s[j])
            output = max(output, j-i+1)
            j += 1

        return output