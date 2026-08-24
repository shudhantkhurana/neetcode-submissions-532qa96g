class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0
        i,j = 0,len(heights)-1
        waterQty = lambda i,j : min(heights[i], heights[j])*(j-i)
        while i < j:
            maxWater = max(maxWater, waterQty(i, j))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxWater
