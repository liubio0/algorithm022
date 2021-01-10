class Solution:

	def jump(self, nums: List[int]) -> int:
		"""
		����������Ż�
		"""
        result = 0 #���
        last_max = 0	#��һ���ܵ������Զλ��
        current_max = 0 #��ǰ�ܵ������Զλ��
        for i in range(len(nums) - 1):  #���һλ������
            current_max = max(nums[i] + i, current_max)
            if i == last_max :
                last_max = current_max
                result += 1
        return result
		
		
    def jump(self, nums: List[int]) -> int:
        """
		��һ������
        1�����⣺����ֵ�ķ�Χ����Ծ����ô�����ٲ��������һ����
        2��˼·��
            1���������飬�������е���ֵ���������ɵ����λ�á�
            2���ڵ�ǰ���ɵ���ֵ�ķ�Χ�ڣ�ѡȡ��һ��������Զ��ֵ��
            3��ѡȡһ�Σ�����һ��ֵ��
        """
        n = len(nums)

        i, result, arrive_max = 0, 0, 0

        while i <= n-1:
            if arrive_max >= n -1: return result
            temp = arrive_max
            arrive_max = max(nums[j] + j for j in range(i, arrive_max+1))
            result += 1
            i = temp + 1	#���ϴ����λ�õ���һλ�ÿ�ʼ�µ�һ��ѭ��
		
[1]
[1,2]
[1,1,1,1]
[1,1,1,1,1]
[2,3,1,1,4]
[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]