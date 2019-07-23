"""
Question:
	Coin Change
See:
	https://leetcode.com/problems/coin-change/
"""
import bisect
from typing import List
from common.verification import Verification


class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:

		dp = [0] * len(nums)
		l = 0
		for n in nums:
			i = bisect.bisect(dp, n, 0, l)
			if i == l:
				l += 1
			dp[i] = n
		return l

	def lengthOfLIS2(self, nums: List[int]) -> int:

		n = len(nums)
		if n == 0:
			return 0

		longest = [1] * n
		for i in range(1, n):
			for j in range(i):
				if nums[i] > nums[j]:
					longest[i] = max(longest[i], longest[j] + 1)
		return max(longest)



if __name__ == "__main__":

	inputs = [
		[[10, 9, 2, 5, 3, 7, 101, 18]],
	]
	targets = [
		4,
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.lengthOfLIS(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
