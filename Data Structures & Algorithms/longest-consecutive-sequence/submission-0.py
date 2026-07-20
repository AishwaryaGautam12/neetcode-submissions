class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i]-1 not in hashset:
                length = 1
                while length+nums[i] in hashset:
                    length += 1
                longest = max(length, longest)

        return longest
        