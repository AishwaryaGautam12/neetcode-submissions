class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        hashset = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in hashset:
                count = 1

                while nums[i]+count in hashset:
                    count += 1

                output = max(output, count)

        return output

        