class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for i in t:
            if i not in hashmap:
                return False
            hashmap[i] -= 1
            if hashmap[i] < 0:
                return False

        return True
                
        