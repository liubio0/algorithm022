class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        思路：bfs
        """
        char_list = [chr(ord('a') + i) for i in range(26)]
        word_set = set(wordList)

        if endWord not in word_set: return 0

        step = 1
        queue, length = collections.deque(), len(beginWord) 
        queue.append(beginWord)

        while queue:
            level_len = len(queue)
            for item in range(level_len):
                head = queue.popleft()
                for i in range(length):
                    for char in char_list:
                        if char == head[i]: continue
                        temp = head[:i] + char + head[i+1:]
                        if temp == endWord: return step + 1
                        if temp in word_set : 
                            queue.append(temp)
                            word_set.remove(temp)
            step += 1
        return 0