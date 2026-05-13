class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_range = len(nums)
        nu = set(nums)

        nums_set = set()
        i = 0

        while i <= n_range: # O(n)
            nums_set.add(i)
            i += 1

        missing = -1
        for x in nums_set: # O(n)
            if x not in nu: # O(1)
                missing = x
                break
        
        return missing
        