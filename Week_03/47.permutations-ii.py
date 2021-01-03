class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        my_dict = {i:1 for i in itertools.permutations(nums, len(nums))}
        return list(my_dict.keys())