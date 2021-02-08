'''
1、读题：
    dp
2、思路：
    1）dp[n] = dp[n-1] + d[n-2]
    2）哨兵dp[0]
    3）2个临时变量减少空间使用
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        f0, f1 = 0, 1
        for i in range(1, n + 1):
            res = f0 + f1
            f0, f1 = f1, res
        return res