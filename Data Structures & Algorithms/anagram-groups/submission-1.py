class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            isort = "".join(sorted(i))
            hashmap[isort].append(i)

        return list(hashmap.values())
        