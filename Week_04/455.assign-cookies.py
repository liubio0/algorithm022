class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        1、读题，双数组比对，取最小满足的匹配。
        2、思路：
            1）排序。
            2）同时遍历数组g和s，满足条件时结果加1并同时移动(用双向队列)。
            3）不满足条件时，移动s。
        3、优化思路：
            双层循环中的和队列优化为单层循环和指针移动。
        """

        s.sort()    #饼干尺寸
        g.sort()    #小孩胃口
        len_s = len(s)
        len_g = len(g)

        i_cookie, i_child = 0, 0

        for i_cookie in range(len_s):
            if i_child > len_g - 1: break
            if s[i_cookie] >= g[i_child]: i_child += 1

        return i_child