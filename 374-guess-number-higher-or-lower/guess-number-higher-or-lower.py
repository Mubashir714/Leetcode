# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=0,n
        while True:
            mid= (l+r)//2
            value=guess(mid)
            if value==-1:
                r=mid-1
            elif value==1:
                l=mid+1
            else:
                return mid
  
