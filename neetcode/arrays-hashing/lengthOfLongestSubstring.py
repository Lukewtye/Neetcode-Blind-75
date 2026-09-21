#approach: sliding window
#complexity: O(n) speed, o(N) space

from typing import List 

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		last = {}      
		left = 0       
		best = 0

		for right, ch in enumerate(s):
			if ch in last and last[ch] >= left:
				left = last[ch] + 1
			last[ch] = right
			best = max(best, right - left + 1)

		return best

if __name__ == "__main__":
	s = Solution()
	assert s.lengthOfLongestSubstring("abcabcbb") == 3
	assert s.lengthOfLongestSubstring("bbbbb") == 1
	print("ok")
