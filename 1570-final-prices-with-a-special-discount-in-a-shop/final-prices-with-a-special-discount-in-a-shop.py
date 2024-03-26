class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for i in range(len(prices)):
            while stack and prices[i]<=prices[stack[-1]]:
                value=stack.pop()
                prices[value]-=prices[i]
            stack.append(i)
        return prices 