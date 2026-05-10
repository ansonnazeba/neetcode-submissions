class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target > mid_val -> go left
        # if target < mid_val -> go right
        # else target == mid_val -> return the mid_index

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        
        return -1