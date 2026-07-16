class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hashmap = {}

        for i in strs:
            isort = "".join(sorted(i))
            if isort not in hashmap:
                hashmap[isort] = [i]
            else:
                hashmap[isort].append(i)

        for i in hashmap:
            output.append(hashmap[i])

        return output
        