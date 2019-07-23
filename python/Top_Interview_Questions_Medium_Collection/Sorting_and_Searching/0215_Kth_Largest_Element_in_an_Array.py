"""
Question:
	Kth Largest Element in an Array

See:
	https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
import collections
import heapq
from typing import List
from common.verification import Verification


class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		return sorted(nums)[-k]


if __name__ == "__main__":

	inputs = [
		[[3, 2, 1, 5, 6, 4], 2],
		[[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
	]
	targets = [
		5,
		4
	]

	s = Solution()
	answers = []
	for i in inputs:
		output = s.findKthLargest(*i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()
