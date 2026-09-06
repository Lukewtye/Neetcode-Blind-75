#approach: sort function pythonically, check neighbors starting with index 1 for 
#similar values.
#complexity: time: O(n log n) space: O(n)

from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortednums = sorted(nums)
        n = 1
        if sortednums == "":
            return False
        for n in range(1, len(sortednums)):
            if sortednums[n] == sortednums[n-1]:
                return True
        return False
        
if __name__ == "__main__":
	s = Solution()
	assert s.hasDuplicate([1,2,3,3]) == True
	assert s.hasDuplicate([1,2,3,4]) == False
	print("ok")
