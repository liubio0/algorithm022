class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
		"""
		1、对arr1中出现在arr2中的元素计数排序，
		2、将arr1中剩余元素排序，与1中的结果拼接。
		"""
        arr2_dict = collections.OrderedDict({i: 0 for i in arr2})
        result_list_1 = []
        for item in arr1:
            if item in arr2_dict: arr2_dict[item] += 1
            else: result_list_1.append(item)
        result_list_2 = []
        for k in arr2_dict:
            result_list_2 += [k]*arr2_dict[k] 
        return result_list_2 + sorted(result_list_1)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        计数排序
        """
        count = [0 for _ in range(1001)]

        res = []
        for item in arr1:   #计数
            count[item] += 1
        
        for item in arr2:   #按arr2排序输出
            if count[item] > 0:
                res += [item] * count[item]
                count[item] -= count[item]
        
        for i in range(len(count)): #剩余的元素排序输入
            if count[i] > 0:
                res += [i] * count[i]

        return res