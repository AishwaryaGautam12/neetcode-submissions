class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        output = float('inf')

        while low <= high:
            if nums[low] < nums[high]:
                output = min(output, nums[low])
                
            mid = (low+high) // 2
            output = min(output, nums[mid])

            if nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid-1

        return output
        