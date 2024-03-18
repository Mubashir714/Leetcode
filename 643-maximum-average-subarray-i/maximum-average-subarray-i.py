class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=maximum=sum(nums[:k])
        l=0
        for r in range(k,len(nums)):
            total+=nums[r]-nums[l]
            maximum=max(maximum,total)
            l+=1
        return maximum/k
