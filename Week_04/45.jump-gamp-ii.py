class Solution:

	def jump(self, nums: List[int]) -> int:
		"""
		参照题解后的优化
		"""
        result = 0 #结果
        last_max = 0	#上一次能到达的最远位置
        current_max = 0 #当前能到达的最远位置
        for i in range(len(nums) - 1):  #最后一位不用跳
            current_max = max(nums[i] + i, current_max)
            if i == last_max :
                last_max = current_max
                result += 1
        return result
		
		
    def jump(self, nums: List[int]) -> int:
        """
		第一遍死磕
        1、读题：数组值的范围内跳跃，怎么用最少步跳到最后一步。
        2、思路：
            1）遍历数组，根据已有的数值来更新最大可到达的位置。
            2）在当前最大可到达值的范围内，选取下一个能走最远的值。
            3）选取一次，更新一次值。
        """
        n = len(nums)

        i, result, arrive_max = 0, 0, 0

        while i <= n-1:
            if arrive_max >= n -1: return result
            temp = arrive_max
            arrive_max = max(nums[j] + j for j in range(i, arrive_max+1))
            result += 1
            i = temp + 1	#从上次最大位置的下一位置开始新的一轮循环
		
[1]
[1,2]
[1,1,1,1]
[1,1,1,1,1]
[2,3,1,1,4]
[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]