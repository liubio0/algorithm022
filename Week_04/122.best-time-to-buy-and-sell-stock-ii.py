class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            读题：买之前必须卖，计算最大获利
            思路：贪心算法，逐天计算获利。
        """
        if len(prices) <= 1 : return 0
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: result += prices[i] - prices[i-1]
        return result