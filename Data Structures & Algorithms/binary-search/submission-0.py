class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target > mid_val -> go left
        # if target < mid_val -> go right
        # else target == mid_val -> return the mid_index

        return self.binary(nums, target, 0, len(nums) - 1)

    def binary(self, nums: List[int], target: int, start: int, end: int):
        if start > end:
            return -1

        mid_ind = (start + end) // 2
        mid_val = nums[mid_ind]

        if target > mid_val:
            return self.binary(nums, target, mid_ind + 1, end)
        elif target < mid_val:
            return self.binary(nums, target, start, mid_ind - 1)

        return mid_ind