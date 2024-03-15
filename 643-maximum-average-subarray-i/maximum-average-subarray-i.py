class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = max_avg = sum(nums[:k])  # sum of the initial window
        
        for i in range(k, len(nums)):
            # get the new sum without re-loop over k
            avg = avg + (nums[i] - nums[i-k])
            if avg > max_avg:
                max_avg = avg

        return max_avg / k  # average

       