class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1、读题
        2、思路
            dfs，找到一个岛屿消灭一个：遍历找到"1"结果加1，置0，然后递推找到上下左右相邻的1陆地，全部置为0。
        3、优化剪枝
            找到一个岛屿消灭岛屿是进行标记，标记为"2"，标记法可以拓展解决同类岛屿问题。
        """
        def delete_one(i, j):
            #上下的左右边界条件判断
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) : return
            #递归结束条件
            if grid[i][j] != "1": return  #值不为0不再递归
            grid[i][j] = "2"
            delete_one(i-1, j)
            delete_one(i+1, j)
            delete_one(i, j-1)
            delete_one(i, j+1)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1": 
                    result += 1
                    delete_one(i, j)
        return result