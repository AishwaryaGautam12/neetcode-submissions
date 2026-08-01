class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        pre = 1

        for i in range(1,len(nums)):
            pre *= nums[i-1]
            output.append(pre)

        suffix = 1

        for i in range(len(nums)-2,-1,-1):
            suffix *= nums[i+1]
            output[i] *= suffix

        return output
        