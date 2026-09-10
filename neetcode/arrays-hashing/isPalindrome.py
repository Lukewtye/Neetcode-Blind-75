#Approach: Filter out bad characters, iterate over string, compare.
#Complexity: Slow, Memory: Great (no more analysis)
from typing import List
#Complexity: Slow, Memory: Great (no more analysis)
#Approach: Filter out bad characters, iterate over string, compare.



class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvqwxyz0123456789"
        compare = ""
        s = s.lower()
        for char in s:
            if char in alphabet:
                compare += char
        reverse = compare[::-1]

        if compare == reverse:
            return True
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("racecar") == True
    assert s.isPalindrome("tacocat") == True
    assert s.isPalindrome("Was it a car or a cat I saw?")  == True
    print("ok")
