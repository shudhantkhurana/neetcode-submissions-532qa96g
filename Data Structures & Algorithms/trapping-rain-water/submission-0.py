class Solution:
    def trap(self, height: List[int]) -> int:

        def findMax(height,N):
            maxValue = -1
            maxIdx = -1
            for i in range(N):
                if height[i] >= maxValue:
                    maxValue = height[i]
                    maxIdx = i
            return maxValue, maxIdx

        N = len(height)
        maxWater = [0]*N
        if N == 1 or N == 2:
            return 0
        i,j = 0,1
        while i < N and j<N:
            if height[i] > height[j]:
                maxWater[j] = height[i]-height[j]
            else:
                i = j
                j = i
            j += 1
        maxValue,maxIdx = findMax(height,N)
        i,j = N-1, N-2
        maxWater[-1] = 0

        while j>=maxIdx:
            if height[j] >= height[i]:
                maxWater[j] = 0
                i = j
                j = i
            else:
                maxWater[j] = height[i] - height[j]
            j -= 1
        return sum(maxWater)