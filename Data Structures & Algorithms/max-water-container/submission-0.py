class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        vol = 0

        while i < j:
            if heights[i] < heights[j]:
                vol = max(vol,heights[i]*(j-i))
                i += 1
            elif heights[i] > heights[j]:
                vol = max(vol,heights[j]*(j-i))
                j -= 1
            else:
                vol = max(vol,min(heights[i],heights[j])*(j-i))
                i += 1

        return vol
        