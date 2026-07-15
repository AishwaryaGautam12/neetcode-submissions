class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni = set()

        for i in nums:
            if i in uni:
                return True
            else:
                uni.add(i)

        return False
        