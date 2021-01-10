class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        1、读题：数组值得范围内跳跃，能否到最后一步
        2、思路：
            1）有0才有可能跳不到终点。
            2）遍历数组，根据已有的数值来更新最大可到达的位置，当最大可到达的位置大于等于最后一位时即返回。
        """
        n = len(nums)
        if n == 0 or min(nums) > 0: return True

        result_max = 0
        for i in range(n):
            result_max = max(i + nums[i], result_max)
            if result_max >= n -1: return True  #注意最后一位为0也可以到达，所以该判断条件要先于下一判断条件。
            if nums[i] == 0 and result_max == i: return False