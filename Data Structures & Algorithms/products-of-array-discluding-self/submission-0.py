class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        prod = 1

        i = 1
        while i < len(nums):
            prod = prod*nums[i-1]
            pre[i] = prod
            i += 1

        output = [1]*len(nums)
        output[-1] = pre[-1]

        post = [1]*len(nums)
        prod = 1

        i = len(nums)-2
        while i >= 0:
            prod = prod*nums[i+1]
            post[i] = prod
            output[i] = post[i]*pre[i]
            i -= 1

        return output

