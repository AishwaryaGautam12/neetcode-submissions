class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1 #we want to map ascii value of c to a number in between 0-26 (count array). lets say ascii of a = 80, b = 81 so for b to be at index 1 we can do b-a 81-80.

            hashmap[tuple(count)].append(s)

        return list(hashmap.values())

