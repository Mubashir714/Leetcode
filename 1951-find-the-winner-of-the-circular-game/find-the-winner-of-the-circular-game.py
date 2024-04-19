class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q= deque([x+1 for x in range(n)])
        while len(q) > 1:
            c=k-1
            while c:
                q.append(q.popleft())
                c-=1
            q.popleft()
        return q[0]

        # nums=list(range(1,n+1))
        # i=0
        # while len(nums)>1:
        #     i=(i+k-1) % len(nums)
        #     nums.pop(i)
        # return nums[0]
