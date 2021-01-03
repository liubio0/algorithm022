class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1),k))

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        1、读题：1-n的k个数组合。
        2、思路：参照题解的回溯，不太理解
        """
        def dfs(n, k, start, result, path):
            if len(path) == k: 
                result.append(path[:])
            
            if len(path) > k: return

            for i in range(start, n + 1):
                path.append(i)
                dfs(n, k, i + 1 , result, path)
                #深度优先遍历记录路径，递归之后需要做相同操作的逆向操作
                path.pop()

        result, path = [], []
        dfs(n, k, 1, result, path)
        return result

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        1、读题：1-n的k个数组合。
        2、优化思路：便利时如果剩余可选长度不够深度，则不需要遍历
        """
        def dfs(n, k, start, result, path):
            if len(path) == k: 
                result.append(path[:])
            
            if len(path) > k: return

            for i in range(start, n + 1 - (k - len(path) - 1)):
                path.append(i)
                dfs(n, k, i + 1 , result, path)
                #深度优先遍历记录路径，递归之后需要做相同操作的逆向操作
                path.pop()

        result, path = [], []
        dfs(n, k, 1, result, path)
        return result
