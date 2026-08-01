class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        pre = 1

        for i in range(1,len(nums)):
            pre *= nums[i-1]
            prefix.append(pre)

        output = [1]*len(nums)
        output[-1] = prefix[-1]
        suffix = 1

        for i in range(len(nums)-2,-1,-1):
            suffix *= nums[i+1]
            output[i] = prefix[i]*suffix

        return output
        