class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        读题：生成n个括号对，求所有有效组合
        思路：
            1）递归，2n个路径，按照深度优先的逻辑，递推选择每一层的括号
        """
        def dfs(level, result, path):
            left_cnt, right_cnt = path.count('('), path.count(')')
            #recursion terminator 
            if level > 2*n and left_cnt == right_cnt:
                result.append(path[:])
                return None
            #process logic in current level
            if left_cnt > n or right_cnt > n: return None
            if right_cnt > left_cnt: return None

            #drill down
            dfs(level + 1, result, path + '(')
            dfs(level + 1, result, path + ')')

            #reverse the current level status if needed
        
        result, path = [], ''
        dfs(1, result, path)
        return result
		
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        思路：dp。
            1）状态：截止到n对括号时的结果
            2）dp方程：dp[n] = "(" + dp[p] ")" + db[q]，其中p是0到n-1的遍历，q是 n-1-p的遍历。
        """
        dp = [[] for _ in range(n + 1) ]
        dp[0] = [""]
        
        for i in range(1, n + 1):
            for p in range(i):
                for inner in dp[p]:
                    for outer in dp[i - p - 1]:                
                        dp[i].append("({0}){1}".format(inner, outer))
        return dp[n]