class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        1�����⣺����ֵ�÷�Χ����Ծ���ܷ����һ��
        2��˼·��
            1����0���п����������յ㡣
            2���������飬�������е���ֵ���������ɵ����λ�ã������ɵ����λ�ô��ڵ������һλʱ�����ء�
        """
        n = len(nums)
        if n == 0 or min(nums) > 0: return True

        result_max = 0
        for i in range(n):
            result_max = max(i + nums[i], result_max)
            if result_max >= n -1: return True  #ע�����һλΪ0Ҳ���Ե�����Ը��ж�����Ҫ������һ�ж�������
            if nums[i] == 0 and result_max == i: return False