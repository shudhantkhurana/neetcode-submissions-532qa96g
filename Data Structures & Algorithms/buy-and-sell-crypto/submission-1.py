class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 1:
            return 0
        i,j = 0,1
        maxProfit = 0
        while i<j and j<N:
            if prices[j] <= prices[i]:
                i = j
                j = i
            else:
                maxProfit = max(maxProfit, prices[j]-prices[i])
            j += 1

        return maxProfit
