class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                target = -nums[i]
                if nums[j]+nums[k] > target:
                    k -= 1
                elif nums[j]+nums[k] < target:
                    j += 1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return output
            

        