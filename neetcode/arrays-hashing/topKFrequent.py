#approach: Filter for frequency, filter for unique, return first k elements.
#complexity: time: o(n log n) memory o(n) 
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_list = sorted(nums, key=counts.get, reverse=True)
        unique = []
        for num in sorted_list:
            if num not in unique:
                unique.append(num)
                if len(unique) == k:
                    return unique

if __name__ == "__main__":
        s = Solution()
        assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
        assert s.topKFrequent([1,2,2,3,3,3], 2) == [3,2]
        assert s.topKFrequent([7,7], 1) == [7]
        print("ok")

