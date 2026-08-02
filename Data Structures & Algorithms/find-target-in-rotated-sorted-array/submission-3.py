class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        output = -1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high

            if nums[low] <= nums[mid]:
                if target < nums[low]:
                    low = mid+1
                elif target > nums[mid]:
                    low = mid+1
                elif target > nums[low] and target < nums[mid]:
                    high = mid-1
            elif nums[high] > nums[mid]:
                if target < nums[mid]:
                    high = mid-1
                elif target > nums[high]:
                    high = mid-1
                elif target < nums[high] and target > nums[mid]:
                    low = mid+1

        return -1

        