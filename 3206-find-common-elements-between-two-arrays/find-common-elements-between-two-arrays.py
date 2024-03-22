class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=count2=0
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count1+=1
        res.append(count1)
        
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                count2+=1
        res.append(count2)
        return res