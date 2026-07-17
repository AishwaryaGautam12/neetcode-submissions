class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1

        freq = [[] for i in range(len(nums))]

        for i in hashmap:
            freq[hashmap[i]-1].append(i)

        output = []
        
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
            
            


        