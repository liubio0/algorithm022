class Solution:

    def mergeSort(self, arr, left, right):
        if left >= right: return 0
        mid = (left + right) >> 1

        count = self.mergeSort(arr, left, mid) + self.mergeSort(arr, mid+1, right)
        
        i, j, k, temp = left, mid + 1, 0, [None] * (right - left + 1)

        while i <= mid and j <= right:
            if (arr[i] / 2)  > arr[j]: 
                count += mid - i + 1
                j += 1
            else:
                i += 1
        i, j = left, mid + 1
		
        while i <= mid and j <= right: 
            if arr[i] <= arr[j]: 
                temp[k] = arr[i]
                i += 1
            else:                
                temp[k] = arr[j]
                j += 1
            k += 1
        while i <= mid: 
            temp[k] = arr[i]
            k += 1
            i += 1

        while j <= right: 
            temp[k] = arr[j]
            k += 1
            j += 1
        
        for p in range(len(temp)): arr[left + p] = temp[p]

        return count

    def reversePairs(self, nums: List[int]) -> int:
        """
        归并排序
        """
        
        return self.mergeSort(nums, 0, len(nums)-1)

########################
class Solution:

    def mergeSort(self, arr, left, right):
        if left >= right: return 0
        mid = (left + right) >> 1

        count = self.mergeSort(arr, left, mid) + self.mergeSort(arr, mid+1, right)
        
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if (arr[i] / 2)  > arr[j]: 
                count += mid - i + 1
                j += 1
            else:
                i += 1

        arr[left: right + 1] = sorted(arr[left: right + 1])

        return count

    def reversePairs(self, nums: List[int]) -> int:
        """
        归并排序，调用系统排序合并（简化了代码，但时间复杂度有提升）【力扣提交时反而时间更短，不理解】
        """
        
        return self.mergeSort(nums, 0, len(nums)-1)