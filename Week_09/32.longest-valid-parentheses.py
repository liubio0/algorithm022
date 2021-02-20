class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        1、维护一个栈，栈顶元素为最近一个未消除的右括号
            1）初始化栈，-1进栈作为哨兵。
            2）遍历括号字符串：
                2.1）遇到（，下标入栈。
                2.2）遇到），栈顶出栈。
                    2.2.1）栈为空，说明配对失败，被出栈的是哨兵、或者上一个未匹配的右括号下标，将该右括号下标入栈，作为最近一个未配对右括号的下标。
                    2.2.2）栈不为空，说明消除成功，更新最大长度（当前下标值 - 栈顶值）。
        """

        tempLen, maxLen = 0, 0
        deque = [-1]

        for i in range(len(s)):
            if s[i] == '(': 
                deque.append(i)
            else: 
                deque.pop()
                if not deque: deque.append(i)
                else: maxLen = max(maxLen, i - deque[-1])
        return maxLen