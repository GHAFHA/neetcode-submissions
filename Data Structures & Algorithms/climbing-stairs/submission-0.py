# what kind of a problem is this ?
# a 1 dimensional problem, it is called this because each subproblem is identified by just one value
class Solution:
    def climbStairs(self, n: int) -> int:
        # how many ways to get to 1 ? just one
        # how many ways to get to 2 ? just two
        # what smaller problem would let me get to the right answer
        if n <= 2:
            return n

        # if we want to get to n, we can either come from n-1 or n-2
        # so the number of ways to get to n is the sum of the ways to get to n-1 and n-2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # we return the number at n, we calculate up to n + 1
        return dp[n]