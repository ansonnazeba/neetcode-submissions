import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        print(maxHeap)
        
        curr = -heapq.heappop(maxHeap)

        while len(maxHeap) >= 1:
            x = maxHeap[0]
            if curr > x:
                x = -heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, -(curr - x))
            curr = -heapq.heappop(maxHeap)
        return curr
        




        print(curr)

        return -1




        