class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # find the actual sum
        # find the expected sum
        # return the difference between them
        actual_sum = 0
        for x in nums:
            actual_sum += x
        
        expected_sum = (len(nums) * (len(nums) + 1)) // 2

        
        # expected_sum = self.sum(len(nums))

        return expected_sum - actual_sum
    
    def sum(self, x: int) -> int:
        if x == 0:
            return 0
        
        return x + self.sum(x - 1)
        

        

        

        

        