class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort the data
        # continuously find the difference between numbers
        # when the difference isn't == 1, stop and return the average
        nums = sorted(nums)
        slow = 0
        fast = 1
        x = 0

        while fast < len(nums):
            diff = nums[fast] - nums[slow]
            if diff != 1:
                x = (nums[fast] + nums[slow]) // 2
                return x
            slow = fast
            fast += 1
        
        if nums[0] != 0:
            return 0
        elif nums[len(nums) - 1] != len(nums):
            return len(nums)
        

        