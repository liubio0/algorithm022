class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        读题：二维数组找最小路径和
        思路：动态规划，归纳规律找递推公式
            1）每一个格子最小路径=min(左侧, 上方)+自己。
            2）根据公式来计算到达二维数组每一个格子的最小路径和，返回grid[-1][-1]即为答案
        优化：优化空间，直接用grid记录结果。
        """

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == c == 0 : continue
                elif r == 0: grid[r][c] = grid[r][c-1] + + grid[r][c]
                elif c == 0: grid[r][c] = grid[r-1][c] + + grid[r][c]
                else: grid[r][c] = min(grid[r-1][c], grid[r][c-1]) + grid[r][c]
        return grid[-1][-1]