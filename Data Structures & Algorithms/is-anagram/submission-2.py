class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}

        for i in s:
            s_map[i] = 1 + s_map.get(i,0)

        t_map = {}

        for i in t:
            if i not in s_map:
                return False
            if i not in t_map:
                t_map[i] = 1
                continue
            t_map[i] += 1
            if t_map[i] > s_map[i]:
                return False
            
        return True
            
        