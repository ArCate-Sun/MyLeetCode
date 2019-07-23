"""
Question:
	Find Peak Element
See:
	https://leetcode.com/problems/find-peak-element/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def findPeakElement(self, nums: List[int]) -> int:

		if not nums:
			return None

		if len(nums) == 1:
			return 0

		for i in range(1, len(nums) - 1):
			if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
				return i

		if nums[0] > nums[1]:
			return 0

		if nums[-1] > nums[-2]:
			return len(nums) - 1


if __name__ == "__main__":

	inputs = [
		[[1, 2, 3, 1]],
		[[1, 2, 1, 3, 5, 6, 4]],
	]
	targets = [
		2,
		1
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.findPeakElement(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
