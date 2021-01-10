class Solution:
    result = float('inf')

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        if endWord not in wordList: return 0
        
        n = len(wordList)
        word_set = set(wordList)
        if beginWord in wordList: word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)
        step = 1

        while queue:
            current_len = len(queue)
            for i in range(current_len):
                currentWord = queue.popleft()
                for i in range(len(currentWord)):   #逐个字母考虑可交换的节点
                    next_word_list = list(currentWord)
                    for ii in range(26):    #按小写字母替换第i个字母后
                        next_word_list[i] = chr(ord('a') + ii)
                        next_word = ''.join(next_word_list)
                        if next_word in word_set:
                            word_set.remove(next_word)
                            if next_word == endWord:
                                return step + 1
                            queue.append(next_word)
            step += 1

        return 0