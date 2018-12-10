"""
Question:
	Best Time to Buy and Sell Stock
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
"""


class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""

		min_price = None
		max_profit = 0
		for price in prices:
			if min_price is None or price < min_price:
				min_price = price
			elif price - min_price > max_profit:
				max_profit = price - min_price

		return max_profit


if __name__ == "__main__":
	s = Solution()

	input = [7, 1, 5, 3, 6, 4]
	print("Input: %s" % input)
	output = s.maxProfit(input)
	print("Output: %s" % output)

	input = [7, 6, 4, 3, 1]
	print("Input: %s" % input)
	output = s.maxProfit(input)
	print("Output: %s" % output)
