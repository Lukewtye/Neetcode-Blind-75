#approach: check sizes of string, count letters and frequencies, compare. 
#Complexity: Both space and time O(n)
from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s) != len(t):
            return False
        for char in s:
            map1[char] = map1.get(char, 0) + 1 
        
        for char in t:
            map2[char] = map2.get(char, 0) + 1 
        
        if map1 == map2:
            return True
        else:
            return False
if __name__ == "__main__":
	s = Solution()
	assert s.isAnagram("civic", "cciiv") == True
	assert s.isAnagram("hello", "lloeh") == True
	assert s.isAnagram("asdads", "sddsadwa") == False
	print("ok")

