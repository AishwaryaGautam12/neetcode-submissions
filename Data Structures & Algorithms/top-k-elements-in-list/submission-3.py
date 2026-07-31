class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)  

        count = [[] for i in range(len(nums))]
        for i in hashmap:
            count[hashmap[i]-1].append(i)

        print(count)

        output = []
        for i in range(len(count)-1,-1,-1):
            for j in count[i]:
                output.append(j)
                if len(output) == k:
                    return output