class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        n=list(range(1,n+1))
        i=0
        while len(n) > 1:
            i=(i+k-1) % len(n)
            n.pop(i)
        return n[0]

