class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = dict()

        for i, val in enumerate(nums):
            comp = target - val
            if comp in map1:
                return [map1[comp], i]
            map1[val] = i 
        
        return []