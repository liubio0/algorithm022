class Solution:
    def numDecodings(self, s: str) -> int:
        """
        读题：数字映射字母，可解码成的不同的组合的总数。
        思路：
            dp
            状态：每1位数字有2种可能，1是自己单独解码，2是与前一位合并解码。单独解码的范围是1-26，为0只能与前一位结合解码，不但单独并往后解码。
            dp数组：记录到达每一位数字时，每个状态对应的解码组合数。
            状态转移：
                解码失败：返回0
                不能单独解码：dp[n] = dp[n-1]; 
                可以单独解码+与前一位组合解码：dp[n] = dp[n-1] + dp[n-2];  
                前一位为0：dp[n] = dp[n-2]; 
                
        """

        if s[0] == '0': return 0
        n = len(s)
        dp = [1] * (n + 1)

        for i in range(2, n+1):
            if s[i-1] == '0' and s[i-2] not in '12': return 0
            if s[i-2:i] in ('10','20'): dp[i] = dp[i-2] #这里注意是i-1不能独立编码。
            elif '10' < s[i-2:i] <= '26': dp[i] = dp[i-1] + dp[i-2]
            else: dp[i] = dp[i-1]
        return dp[-1]