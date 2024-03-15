class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum= float("-inf")
        l=total=0
        for r in range(len(nums)):
            total+=nums[r]
            if r >= k-1:
                maximum=max(maximum,total)
          
                total-=nums[l]
                l+=1
        return maximum/k

       