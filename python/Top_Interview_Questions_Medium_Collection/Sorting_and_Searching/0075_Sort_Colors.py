"""
Question:
	Sort Colors
See:
	https://leetcode.com/problems/sort-colors/
"""
import collections
from typing import List


from common.verification import Verification


class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		counter = collections.Counter(nums)
		red, white, blue = counter.get(0, 0), counter.get(1, 0), counter.get(2, 0)

		for i in range(red):
			nums[i] = 0
		for i in range(red, red + white):
			nums[i] = 1
		for i in range(red + white, len(nums)):
			nums[i] = 2


if __name__ == "__main__":

	inputs = [
		[[2, 0, 2, 1, 1, 0]],
	]
	targets = [
		[0, 0, 1, 1, 2, 2]
	]

	s = Solution()
	answers = []
	for i in inputs:
		s.sortColors(*i)
		answers.append(*i)

	verification = Verification(inputs, answers, targets)
	verification.verify()
