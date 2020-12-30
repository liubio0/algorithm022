from collections import Counter
import heapq 

class Solution:
    def topKFrequent_new1(self, nums, k):
        """
        读题：求整数数组中前k个出现重复次数最多的元素
        思路：根据国际站思路，Counter得到最高频的k个数，然后根据返回的元组list结构遍历出结果
        """
        return [t[0] for t in Counter(nums).most_common(k)]

    def topKFrequent(self, nums, k):
        """
        读题：求整数数组中前k个出现重复次数最多的元素
        思路：用最小堆来处理
        """
        my_dict = Counter(nums)

        h = []
        for key, cnt in my_dict.items(): 
            if len(h) < k:
                heapq.heappush(h, (cnt, key))
            else :
                heapq.heappushpop(h, (cnt, key))

        return [heapq.heappop(h)[1] for i in range(len(h))]
        

if __name__ == '__main__':
    cls = Solution()
    print(cls.topKFrequent([1,1,1,2,2,2,3],2))