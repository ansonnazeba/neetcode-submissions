class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        set_in = set()

        for i in nums:
            if i in set_in:
                return True
            set_in.add(i)

        return False

        