class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            base = right - left
            height = min(heights[left], heights[right])
            max_area = max(base * height, max_area)

            if (heights[left] >= heights[right]):
                right -= 1
            else:
                left += 1
        
        return max_area


        