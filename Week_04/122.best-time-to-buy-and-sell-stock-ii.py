class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            ���⣺��֮ǰ������������������
            ˼·��̰���㷨��������������
        """
        if len(prices) <= 1 : return 0
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: result += prices[i] - prices[i-1]
        return result