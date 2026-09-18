#Approach: Left and right indices, compute area, move smaller height inward to search for larger area.
#Complexity: O(N) Time, O(1) space

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not list:
            return []
        map = {}
        best = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            best = max((r - l) * min(heights[l], heights[r]), best)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best 

if __name__ == "__main__":
	s = Solution()
	assert s.maxArea([1,7,2,5,4,7,3,6]) == 36
	assert s.maxArea([2,2,2]) == 4
	print("ok")
