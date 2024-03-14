class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        l=0
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                prices[l]=prices[i]
            maximum=max(maximum, prices[i]-prices[l])
        return maximum
            

        
