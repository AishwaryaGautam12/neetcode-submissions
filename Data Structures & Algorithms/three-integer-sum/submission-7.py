class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        i = 0
        while i < len(nums):
            j = i+1
            k = len(nums)-1

            while j < k:
                target = -nums[i]
                if nums[j]+nums[k] > target:
                    k -= 1
                elif nums[j]+nums[k] < target:
                    j += 1
                else:
                    if [nums[i],nums[j],nums[k]] not in output:
                        output.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

            i += 1

        return output
            

        