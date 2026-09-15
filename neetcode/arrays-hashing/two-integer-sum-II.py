#Approach: Compare left and right indices to target, move right down if sum > target, left up otherwise. 
#Complexity: O(N) time, O(1) space

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        l = 0
        r = len(numbers) - 1
        while l < r:
            t = numbers[l] + numbers[r]
            if t == target:
                return [l+1, r + 1]
            elif t > target:
                r -= 1
            else:
                l += 1

if __name__ == "__main__":
	s = Solution()
	assert s.twoSum([1,2,3,4], 3) == [1, 2]
	assert s.twoSum([1,2,5,6], 3) == [1, 2]
	print("ok")
	
