#Approach: consider i as the sell price, update buy price as you traverse the list, calculate max profit and store it.
#Complexity: o(n) time, 0(1) space. Optimal solution. 

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = 100
        for i in range(0, len(prices)):
            buy = min(prices[i], buy)
            best = max((prices[i] - buy), best)
        
        if best > 0:
            return best
        else:
            return 0

if __name__ == "__main__":
	s = Solution()
	assert s.maxProfit([10,1,5,6,7,1]) == 6
	assert s.maxProfit([10,8,7,5,2]) == 0
	assert s.maxProfit([1,5,8,1,10,9]) == 9
	print("ok")


