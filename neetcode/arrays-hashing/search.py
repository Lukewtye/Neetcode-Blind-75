#approach: use pythonic index function
#time: o(N) time, o(1) space

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return (nums.index(target))
        except ValueError:
            return -1

if __name__ == "__main__":
	s = Solution()
	assert s.search(nums = [-1,0,2,4,6,8], target = 4) == 3
	assert s.search(nums = [-1,0,2,4,6,8], target = 3) == -1
	print("ok")
