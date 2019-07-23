"""
Question:
	Longest Increasing Subsequence
See:
	https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List
from common.verification import Verification


class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		coins = list(sorted([c for c in set(coins) if c > 0], reverse=True))
		best = float("inf")

		def getNum(start, count, target):
			nonlocal best
			if count + target // coins[start] + (target % coins[start] != 0) >= best:  # even best case won't beat
				return
			if target % coins[start] == 0:  # this might be good enough
				best = min(best, count + target // coins[start])
			if start == len(coins) - 1:
				return

			for j in range(target // coins[start], -1, -1):
				getNum(start + 1, j + count, target - j * coins[start])

		getNum(0, 0, amount)
		return best if best != float('inf') else -1

	def coinChange2(self, coins: List[int], amount: int) -> int:

		if amount == 0:
			return 0

		dp = [0x7ffffff for i in range(amount + 1)]
		dp[0] = 0
		for i in range(len(coins)):
			for j in range(1, amount + 1):
				if j >= coins[i]:
					dp[j] = min(dp[j], dp[j - coins[i]] + 1)

		if dp[-1] == 0x7ffffff:
			return -1
		return dp[-1]


if __name__ == "__main__":

	inputs = [
		[[1, 2, 5], 11],
		[[2], 3],
		[[186, 419, 83, 408], 6249],
		[[2147483647], 2]
	]
	targets = [
		3,
		-1,
		20,
		-1
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.coinChange(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
