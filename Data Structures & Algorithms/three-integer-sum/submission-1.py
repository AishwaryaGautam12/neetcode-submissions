class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            target = -(nums[i])

            while j < k:
                if nums[j]+nums[k] == target:
                    if [nums[i],nums[j],nums[k]] not in output:
                        output.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif nums[j]+nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return output


        