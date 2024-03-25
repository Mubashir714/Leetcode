class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        array=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                array.append(nums[i])
        return array