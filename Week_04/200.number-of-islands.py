class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1������
        2��˼·
            dfs���ҵ�һ����������һ���������ҵ�"1"�����1����0��Ȼ������ҵ������������ڵ�1½�أ�ȫ����Ϊ0��
        3���Ż�
            �ҵ�һ�������������ǽ��б�ǣ����Ϊ"2"����Ƿ�������չ���ͬ�ൺ�����⡣
        """
        def delete_one(i, j):
            #���µ����ұ߽������ж�
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) : return
            #�ݹ��������
            if grid[i][j] != "1": return  #ֵ��Ϊ0���ٵݹ�
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