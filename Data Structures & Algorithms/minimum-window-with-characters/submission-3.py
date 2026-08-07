class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tmap = {}
        for i in t:
            tmap[i] = 1+tmap.get(i, 0)

        i = 0
        j = 0
        rlen = len(s)
        result = ""
        smap = {}
        cond = 0
        satis = len(tmap)
        while j < len(s):
            smap[s[j]] = 1 + smap.get(s[j],0)
            if s[j] in tmap and tmap[s[j]] == smap[s[j]]:
                cond += 1
            while cond >= satis:
                if j-i+1 <= rlen:
                    rlen = j-i+1
                    result = s[i:j+1]
                smap[s[i]] -= 1
                if s[i] in tmap and tmap[s[i]] > smap[s[i]]:
                    cond -= 1
                i += 1

            j += 1

        return result



        