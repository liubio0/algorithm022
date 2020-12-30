class Solution:
    def nthUglyNumber(self, n) :
        """
        1、读题：
            限定质因子求增长序列
        2、思路：
            根据题解思路，后续的丑数一定是之前所有丑数中的1个数乘以2、3、5中的一个数得来的。不同的丑数乘以2、3、5时可能是跳跃前进、也可能产生相同的结果。
            参照题解，分别维护3个质因子当前进度的下标，用来生成新的一个最小丑数，生成丑数的下标加1。
        3、code
        4、debug、commit
        """
        ret = [1] * n
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            ret[i] = min(min(ret[p2] * 2, ret[p3] * 3), ret[p5] * 5)
            if ret[i] == (ret[p2] * 2) : p2 += 1
            if ret[i] == (ret[p3] * 3) : p3 += 1
            if ret[i] == (ret[p5] * 5) : p5 += 1

        return ret[n-1]

if __name__ == '__main__':
    cls = Solution()
    print(cls.nthUglyNumber(100))
    #1536

    print(cls.nthUglyNumber(1690))
    #2123366400