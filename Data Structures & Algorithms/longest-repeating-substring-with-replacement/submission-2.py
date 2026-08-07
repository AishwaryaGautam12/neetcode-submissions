class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cmap = {}
        result = 0
        i = 0
        j = 0

        while j < len(s):
            cmap[s[j]] = 1 + cmap.get(s[j],0)
            rep = (j-i+1) - max(cmap.values())

            while rep > k:
                cmap[s[i]] -= 1
                i += 1
                rep = (j-i+1) - max(cmap.values())

            result = max(result, j-i+1)
            j += 1

        return result


        