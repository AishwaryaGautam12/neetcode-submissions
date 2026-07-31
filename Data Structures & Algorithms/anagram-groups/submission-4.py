class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sort_s = tuple(sorted(s))
            if sort_s in hashmap:
                hashmap[sort_s].append(s)
            else:
                hashmap[sort_s] = [s]

        return [v for v in hashmap.values()]

