class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        prev1 = 2
        prev2 = 1
        for i in range(2,n):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1
        