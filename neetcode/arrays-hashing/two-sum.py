# Approach: one pass, dict of value -> first index, look for the complement
# Complexity: time O(n), space O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([0, 0], 0) == [0, 1]      # duplicate values
    assert s.twoSum([3, 2, 4], 6) == [1, 2]   # first element is a decoy
    assert s.twoSum([], 0) == []              # empty input
    print("ok")
