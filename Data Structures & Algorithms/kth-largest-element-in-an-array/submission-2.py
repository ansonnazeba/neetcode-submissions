import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # add elements to a heap
        # pop from the heap k -1 times
        heapq.heapify(nums) # build heap

        i = len(nums)
        while i > k:
            heapq.heappop(nums) 
            i -= 1

        return heapq.heappop(nums)


        