class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
		"""
		系统函数排序
		"""
        return sorted(s) == sorted(t)
		
    def isAnagram(self, s: str, t: str) -> bool:
		"""
		哈希映射
		"""
		
        if len(s) != len(t) : return False

        my_dict = [0] * 26
        for i in range(len(s)):
            my_dict[ord(s[i]) - ord('a')] += 1
            my_dict[ord(t[i]) - ord('a')] -= 1
        
        for i in my_dict:
            if i != 0: return False

        return True