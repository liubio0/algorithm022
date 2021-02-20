class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        寻找最长严格递增子序列

        思路1：当前已存在的长子序列集合中的最后一个元素，与最新元素比较。
            1）状态定义：dp = 到达第i位时的最长子序列长度。
        """
        if len(nums) <= 1: return len(nums)

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
		
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        寻找最长严格递增子序列

        思路2：维护一个结果列表，使用二分查找确定新的元素在结果列表中的位置。
            1）比结果列表中的值小，替换结果列表中比该元素大的第一个下标元素。
            2）比结果列表的值都大，则添加到已有元素的末尾。
            3）结果列表的长度，即为已找到的最长严格递增子序列的长度。
        """

        dp = []
        for num in nums:
            idx = bisect_left(dp, num)
            if idx == len(dp): dp.append(num)
            else: dp[idx] = num
        return len(dp)