"""
Question:
	Best Time to Buy and Sell Stock II
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
"""


class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""

		profit = 0

		if len(prices) > 0:

			purchase_price = None
			for i in range(1, len(prices)):
				if prices[i - 1] > prices[i] and purchase_price is not None:
					# 昨日的价高于今日的价, 并且手中持股, 昨日应该卖出
					profit += prices[i - 1] - purchase_price
					purchase_price = None
				elif prices[i - 1] < prices[i] and purchase_price is None:
					# 昨日的价低于今日的价, 并且手中无股, 昨日应该买进
					purchase_price = prices[i - 1]

			if purchase_price is not None:
				# 如果最后一天时手中持股, 则卖掉
				profit += prices[i] - purchase_price

		return profit


if __name__ == "__main__":
	s = Solution()

	prices = [7, 1, 5, 3, 6, 4]
	profit = s.maxProfit(prices)
	print("Input: %s" % prices)
	print("Output: %s" % profit)

	prices = [1, 2, 3, 4, 5]
	profit = s.maxProfit(prices)
	print("Input: %s" % prices)
	print("Output: %s" % profit)

	prices = [7, 6, 4, 3, 1]
	profit = s.maxProfit(prices)
	print("Input: %s" % prices)
	print("Output: %s" % profit)
