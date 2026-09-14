#Approach: Sort, iterate, skip over repeats and get longest length
#Complexity: O(n log n)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        best = 1
        temp = 1
        for i in range (1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == 1 + nums[i - 1]:
                temp += 1
                best = max(temp, best)
            else:
                temp = 1
        return best
if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([2,20,4,10,3,4,5]) == 4
    assert s.longestConsecutive([0,3,2,5,4,6,1,1]) == 7
    print("ok")

