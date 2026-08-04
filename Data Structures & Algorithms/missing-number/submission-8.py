class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # find the actual sum
        # find the expected sum
        # return the difference between them
        actual_sum = 0
        for x in nums:
            actual_sum += x
        
        expected_sum = (len(nums) * (len(nums) + 1)) // 2

        return expected_sum - actual_sum
        

        

        

        

        