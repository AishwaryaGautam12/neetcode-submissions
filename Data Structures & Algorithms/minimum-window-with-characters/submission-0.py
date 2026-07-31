class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = float("infinity")
        output = ""

        if len(t) > len(s):
            return ""
        
        needmap = {}
        for i in t:
            needmap[i] = 1 + needmap.get(i, 0)

        i = 0
        have = 0
        need = len(needmap)
        havemap = {}

        for j in range(len(s)):
            havemap[s[j]] = 1 + havemap.get(s[j],0)
            if s[j] in needmap and havemap[s[j]] == needmap[s[j]]:
                have += 1

            while have == need:
                if j-i+1 < length:
                    output = s[i:j+1]
                    length = j-i+1

                havemap[s[i]] -= 1
                if s[i] in needmap and havemap[s[i]] < needmap[s[i]]:
                    have -= 1
                i += 1
 
        return output